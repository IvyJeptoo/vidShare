from django.urls import path,include
from . import views
from .views import *

urlpatterns=[
    path('',views.index, name='index'),
    path('signup/',SignUpView.as_view(),name='signup'),
    path('home',views.home, name='home'),
    path('viewProfile',views.viewProfile, name='viewProfile'),
    path('postVideo',views.postVideo, name='postVideo'),
    path('video/<id>',views.comment, name='comment'),
    path('like/<id>', views.like_post,name='like'),
    path('unfollow/<to_unfollow>', views.unfollow, name='unfollow'),
    path('follow/<to_follow>', views.follow, name='follow'),





]