from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('app_entry/', views.app_entry, name='app_entry'),
    path('profile/', views.profile, name='profile'),
    path('profile_App/', views.profile_App, name='profile_App'),
    

]