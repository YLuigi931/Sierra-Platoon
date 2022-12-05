from django.urls import path
from . import views

# GET       --- read
# POST      --- create
# PUT       --- update
# DELETE    --- delete
# PATCH     --- update a part of object

# api/ helps differenciate the routes we used on the frontend

urlpatterns = [
    path('', views.index),
    path('api/categories/', views.categories),
    path('api/categories/<int:category_id>',views.category), # a single category
    path('api/posts/', views.posts),
    path('api/posts/<int:post_id>',views.post),
    path('api/categories/<int:category_id>/posts',views.category_posts),
    path('api/categories/<int:category_id>/posts/<int:post_id>',views.post_by_category),
    
]
