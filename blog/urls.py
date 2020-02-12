from django.contrib import admin
from django.urls import path,include
#from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
#from .views import SignUpView 
from . import views
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView


app_name='blog'
urlpatterns = [
	
    path('',views.post_list,name='post_list'),
	path('home/',views.home,name='home'),
	path('post_new/',views.post_new,name='post_new'),
	
    path('login/',LoginView.as_view(),name='login'),
    path('myblogs/',views.myblogs,name='myblogs'),
    #path('password_reset/', ,name='password_reset'),
    path('signup/',views.signup, name='signup'),
    path('logout/',views.log_out,name='logout'),
    #path('logout/', views.LogoutView.as_view(), name='logout'),

    path('password-reset/', PasswordResetView.as_view(template_name='blog/password_reset_form.html',
        subject_template_name='blog/password-reset/password_reset_subject.txt',email_template_name='blog/password-reset/password_reset_email.html'),name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='blog/password-reset/password_reset_done.html'), name='password_reset_done'),
    #**for comment -----
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'), #for comment
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),      #for comment
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='blog/password-reset/password_reset_complete.html'), name='password_reset_complete'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='blog/password-reset/password_reset_confirm.html'), name='password_reset_confirm'),
    
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'), #for comment
    #path('post/<int:pk>/reply/', views.reply, name='add_comment_to_post'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('<int:pk>/detail/', views.post_detail, name='post_detail'),
    path('subscribe/',views.subscribe,name='subscribe'),
    #path('login/')
]