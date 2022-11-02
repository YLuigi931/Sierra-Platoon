from django.urls import path
from . import views
urlpatterns=[
    path('poke/',views.index ),
    path('poke/<int:poke_id>/', views.detail),
]