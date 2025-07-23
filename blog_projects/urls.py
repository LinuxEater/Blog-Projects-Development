from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('category/<int:category_id>/', views.posts_by_category, name='posts_by_category'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    ]