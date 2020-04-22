from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/login/', views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('users/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    path('', include('blog_app.urls'))
]
