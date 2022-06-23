from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.urls import reverse
from django.views import View
from .forms import *
from django.http import HttpResponseRedirect
from .models import *

# Create your views here.
def index(request):
    return render(request, 'main/index.html')
def home(request):
    videos = Video.objects.all()
    
    return render(request, 'main/home.html', {'videos':videos})

class SignUpView(View):
    form_class = SignUpForm
    initial = {'key':'value'}
    template_name = 'registration/signup.html'
    
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request,self.template_name,{'form':form})
    
    def post(self, request,*args,**kwargs):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hey {username}, your account has been created successfully!')
            
            return redirect(to='login')
        
        return render(request,self.template_name,{'form':form})
    
class CustomLoginView(LoginView):
    form_class = LoginView
    
    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        
        if not remember_me:
             # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)
            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True
         # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView,self).form_valid(form)


def viewProfile(request):
    videos = request.user.video.all()
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST,request.FILES,instance=request.user.profile)
        
        
        if profile_form.is_valid() and  user_form.is_valid():             
            userform =  user_form.save(commit=False)         
            profileform = profile_form.save(commit=False)
            profileform.save()
            userform.save()
            return redirect (to='viewProfile')
            # return HttpResponseRedirect(request.path_info)    
    else:
        profile_form = UpdateProfileForm(instance=request.user.profile)
        user_form = UpdateUserForm(instance=request.user)
       
    return render(request,'main/profile.html', {'profile_form': profile_form,'user_form': user_form,'videos':videos })

def postVideo(request):
    current_user = request.user
    if request.method == 'POST':
        video_form = VideoForm(request.POST,request.FILES,instance=request.user.profile)
        if video_form.is_valid():
            video = video_form.save(commit=False)
            video.user = current_user
            video.save()
            return redirect(to='home')
    else:
        video_form = VideoForm()
    context ={
        'video_form': video_form,
            
    }
            
    return render(request, 'main/post.html',context)


def comment(request, id):
    video = get_object_or_404(Video, pk=id)
    comments = video.comment.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.video = video
            comment.user = request.user.profile
            comment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CommentForm()
    params = {
        'video': video,
        'form': form,
        'comments':comments,
    }
    
    return render(request, 'main/comments.html',params)

def like_post(request,id):
    video = Video.objects.get(pk=id)
    is_liked = False
    user=request.user.profile
    try:
        profile=Profile.objects.get(user=user.user)
        print(profile)
    except Profile.DoesNotExist:
        raise Http404()
    if video.likes.filter(id=user.user.id).exists():
        video.likes.remove(user.user)
        is_liked=False
    else:
        video.likes.add(user.user)
        is_liked=True
    return HttpResponseRedirect(reverse('home'))