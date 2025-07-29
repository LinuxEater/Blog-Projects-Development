from django.contrib import admin
from .models import Services

# Register your models here.
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('service_title', 'service_description')
    search_fields = ('service_title', 'service_description')
    list_filter = ('created_at',)
    ordering = ['-created_at']

admin.site.register(Services, ServicesAdmin)
