from django.shortcuts import render
from .models import Blog, Category


# Create your views here.
# blog_projects/templatetags/custom_filters.py


def home(request):
    categories = Category.objects.all()
    blogs = Blog.objects.filter(status='Published')
    blogs_front = Blog.objects.filter(category=5)
    featured_blogs = blogs.filter(is_featured=True)
    context = {
        'blogs': blogs,
        'featured_blogs': featured_blogs,
        'categories': categories,
        'blogs_front': blogs_front,
    }
    return render(request, 'home.html', context)

def posts_by_category(request, category_id):
    categories = Category.objects.all()
    category = Category.objects.get(id=category_id)
    blogs = Blog.objects.filter(category=category, status='Published')
    context = {
        'blogs': blogs,
        'category': category.category_name,
        'categories': categories,
        'selected_category': category,
    }
    return render(request, 'posts_by_category.html', context)

def post_detail(request, slug):
    categories = Category.objects.all()
    technologies = Blog.objects.values_list('technologies', flat=True).distinct()
    blog = Blog.objects.get(slug=slug, status='Published')
    context = {
        'blog': blog,
        'technologies': technologies,
        'categories': categories,
    }
    return render(request, 'single_post_detail.html', context)


def about(request):
    return render(request, 'about.html')