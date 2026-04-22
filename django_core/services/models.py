from django.db import models
class Service(models.Model):        #id is the defauld field in django model which doesn't need to be created.
    name = models.CharField(max_length=100)
    description = models.TextField()
    service_image = models.ImageField(upload_to="services/") 

    def __str__(self):
        return self.name
# Create your models here.
