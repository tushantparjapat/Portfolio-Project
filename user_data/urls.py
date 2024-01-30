from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    
    path('', views.index,name='index'),
    path('login/', views.log_in,name='login'),
    path('signin', views.sign_in,name='signin'),
    path('logout/', views.logout_view,name='logout'),
    path('dashboard/<id>/', views.dashboard,name='dashboard'),
    path('up_dashboard', views.up_dashboard,name='up_dashboard'),
    path('com', views.com,name='com'),
    path('edu_add', views.education_add,name='edu_add'),
    path('edu_delete', views.edu_delete,name='edu_delete'),
    path('project_add', views.project_add,name='project_add'),
    path('project_delete', views.project_delete,name='project_delete'),
    path('exp_add', views.exp_add,name='exp_add'),
    path('exp_delete', views.exp_delete,name='exp_delete'),
    path('skill_add', views.skill_add,name='skill_add'),
    path('skill_delete', views.skill_delete,name='skill_delete'),
    path('profile_edit', views.profile_edit,name='profile_edit'),   
    path('forgot_password', views.forgot_password,name='forgot_password'),   
    path('verify_otp', views.verify_otp,name='verify_otp'),   
    
]