from django.db import models



class contactEnquiry(models.Model):

    SERVICE_CHOICES = [
        ('cleaning', 'Cleaning'),
        ('plumbing', 'Plumbing'),
        ('electrical', 'Electrical'),
        ('ac', 'AC Repair'),
    ]


    name = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    subject = models.CharField(max_length=100)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    message = models.TextField()

# Create your models here.
