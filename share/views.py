from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.views import View
from .forms import *
from django.http import HttpResponseRedirect
from .models import *

# Create your views here.
def index(request):
    return render(request, 'main/index.html')
def home(request):
    return render(request, 'main/home.html')

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
    # posts = request.user.posts.all()
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST,request.FILES,instance=request.user.profile)
        
        
        if profile_form.is_valid() and  user_form.is_valid():             
            user_form.save()         
            profile_form.save()
            return redirect (to='viewProfile')
            # return HttpResponseRedirect(request.path_info)    
    else:
        profile_form = UpdateProfileForm(instance=request.user.profile)
        user_form = UpdateUserForm(instance=request.user)
       
    return render(request,'main/profile.html', {'profile_form': profile_form,'user_form': user_form, })