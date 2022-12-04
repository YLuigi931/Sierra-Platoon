from django.urls import path
from . import views

# GET       --- read
# POST      --- create
# PUT       --- update
# DELETE    --- delete
# PATCH     --- update a part of object


urlpatterns = [
    path('', views.index),
    path('categories/', views.categories),
    path('categories/<int:category_id>',views.category), # a single category
    path('posts/', views.posts),
    path('posts/<int:post_id>',views.post),
    path('categories/<int:category_id>/posts',views.category_posts),
    path('categories/<int:category_id>/posts/<int:post_id>',views.post_by_category),
    
]
