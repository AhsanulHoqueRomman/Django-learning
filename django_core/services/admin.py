from django.contrib import admin
from .models import Service
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name','description','service_image')

admin.site.register(Service, ServiceAdmin)
# Register your models here.
