from django.shortcuts import render
from .models import Blog, Category

# Create your views here.


def home(request):
    categories = Category.objects.all()
    blogs = Blog.objects.filter(status='Published')
    featured_blogs = blogs.filter(is_featured=True)
    context = {
        'blogs': blogs,
        'featured_blogs': featured_blogs,
        'categories': categories,
    }
    return render(request, 'home.html', context)
