from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView


app_name='myapp'

urlpatterns = [
    path('register-user/',RegisterCreateView.as_view(),name='register-user'),
    path('login-user/',LoginCustomView.as_view(),name='login-user'),
    path('logout-user/',LogoutView.as_view(),name='logout-user'),
    
    path('user-profile/<str:pk>/',UserProfileView.as_view(),name='user-profile'),
    path('update-user/<str:pk>/',UserUpdateView.as_view(),name='update-user'),
    path('update-user-infor/<str:pk>/',UserProfileUpdateView.as_view(),name='update-user-infor'),

    path('',HomeView.as_view(),name="home-view"),
    path('rom/<str:pk>/',RomeView.as_view(),name="rom-view"),


    path('create-room/',CreateRoomView.as_view(),name="create-room"),
    path('update-room/<str:pk>/',RomModelUpdateView.as_view(),name="update-room"),
    path('dalete-room/<str:pk>/',RomModelDeleteView.as_view(),name="delete-room"),
]
