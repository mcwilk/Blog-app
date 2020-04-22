from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('posts/<int:pk>/', views.details, name='details'),
    path('posts/new/', views.post_add, name='post_add'),
    path('posts/edit/<int:pk>', views.post_edit, name='post_edit'),
    path('posts/drafts', views.post_drafts , name='post_drafts'),
    path('posts/publish/<int:pk>', views.post_publish, name='post_publish'),
    path('posts/delete/<int:pk>', views.post_delete, name='post_delete'),
    path('posts/draft/delete/<int:pk>', views.draft_delete, name='draft_delete'),
    path('users/signup/', views.signup, name='signup'),
]