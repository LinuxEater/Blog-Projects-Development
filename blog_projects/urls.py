from django.urls import path
from . import views
from blog_projects import views as blog_views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('category/<int:category_id>/', views.posts_by_category, name='posts_by_category'),
    path('post/search/', blog_views.search, name='search'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    
    ]