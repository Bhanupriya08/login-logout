from django.contrib import admin
from django.urls import path,include
#from django.contrib.auth import views as auth_views

#from .views import SignUpView 
from . import views
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView


app_name='blog'
urlpatterns = [
	
	path('',views.home,name='home'),
	path('post_new/',views.post_new,name='post_new'),
	path('post_list/',views.post_list,name='post_list'),
    path('login/',LoginView.as_view(),name='login'),
    #path('password_reset/', ,name='password_reset'),
    path('signup/',views.signup, name='signup'),
    path('logout/',views.log_out,name='logout'),
    #path('logout/', views.LogoutView.as_view(), name='logout'),
    path('password_reset/', PasswordResetView.as_view(template_name='blog/password_reset_form.html',
        subject_template_name='blog/password-reset/password_reset_subject.txt',email_template_name='blog/password-reset/password_reset_email.html'),name='password_reset'),
    path('password/done/', PasswordResetDoneView.as_view(template_name='blog/password-reset/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='blog/password-reset/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(template_name='blog/password-reset/password_reset_complete.html'), name='password_reset_complete'),
    path('myblogs/',views.myblogs,name='myblogs'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('<int:pk>/detail/', views.post_detail, name='post_detail'),
    #path('login/')
]