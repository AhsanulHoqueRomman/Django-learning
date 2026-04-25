from django.contrib import admin
from .models import contactEnquiry

class contactEnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'service','message')

admin.site.register(contactEnquiry)
