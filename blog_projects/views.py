from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Category, Comment
from services.models import Services
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect

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
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')
    categories = Category.objects.all()
    technologies = Blog.objects.values_list('technologies', flat=True).distinct()
    blog = Blog.objects.get(slug=slug, status='Published')
    
    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)
    
    # Comments
    comments = Comment.objects.filter(blog=single_blog)
    comment_count = comments.count()
    
    context = {
        'blog': blog,
        'technologies': technologies,
        'categories': categories,
        'comments': comments,
        'comment_count': comment_count
    }
    
    return render(request, 'single_post_detail.html', context)


def about(request):
    return render(request, 'about.html')

def services(request):
    services = Services.objects.all()
    context = {
        'services':services
    }
    return render(request, 'services.html', context)

def search(request):
    keyword = request.GET.get('keyword', '')  # Default to empty string if no keyword is provided
    
    # Search blogs by title, content, or technologies
    blogs = Blog.objects.filter(
        Q(title__icontains=keyword) |
        Q(url_github__icontains=keyword) |
        Q(technologies__icontains=keyword) |
        Q(blog_body__icontains=keyword) |
        Q(short_description__icontains=keyword),
        status='Published'
    ).distinct()

    # If no blogs are found, return a message in the context
    if not blogs:
        message = f"No results found for '{keyword}'"
    else:
        message = None

    context = {
        'blogs': blogs,
        'message': message,
        'search_query': keyword,
    }

    return render(request, 'search_results.html', context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            print(form.errors)
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('home')
    form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('home')
