from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name_plural = "categories"

STATUS_CHOICES = (
    ('Draft', 'Draft'),
    ('Published', 'Published'),
)

class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    technologies = models.CharField(max_length=200)
    video = models.FileField(upload_to='projects/videos/', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    short_description = models.TextField(max_length=500)
    blog_body = models.TextField(max_length=2000)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES, default='Draft')
    url_demo_live = models.CharField(blank=True, null=True)
    url_github = models.URLField(max_length=255,blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "blogs"
        ordering = ['-created_at']  # Order by creation date descending  