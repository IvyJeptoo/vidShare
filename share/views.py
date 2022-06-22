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
