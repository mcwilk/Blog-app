from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('posts/<int:pk>/', views.details, name='details'),
    path('posts/new/', views.post_add, name='post_add'),
    path('posts/edit/<int:pk>', views.post_edit, name='post_edit'),
]