from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.index),
    # Signup/create user
    path('signup/', views.signup),
]