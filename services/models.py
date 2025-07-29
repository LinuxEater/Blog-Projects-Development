from django.db import models

# Create your models here.

class  Services(models.Model):
    service_title = models.CharField(max_length=100)
    service_description = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.service_title
    
    class Meta:
        verbose_name_plural = "services"
        ordering = ['-created_at']