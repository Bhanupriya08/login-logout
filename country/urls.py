from django.contrib import admin
from django.urls import path,include
from . import views

app_name='country'
urlpatterns = [
	
    
    path('', views.data, name='person_list'),
    
    path('ajax/load-cities/', views.load_states, name='ajax_load_cities'),
    path('getdetails/',views.getdetails),
    path('uploadfile/',views.upload,name='uploadfile'),
    path('booklist/',views.booklist,name='book_list'),
    path('crud/',  views.CrudView.as_view(), name='crud_ajax'),
    path('timer/',views.timerFun,name='timeFun'),
    #path('add/', views.PersonCreateView.as_view(), name='person_add'),
    #path('<int:pk>/', views.PersonUpdateView.as_view(), name='person_change'),

]