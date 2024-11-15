
from django.db import models
from django.urls import reverse

# Create your models here.

class Survey(models.Model):
    question= models.TextField()
    option_a= models.TextField()
    option_b= models.TextField()
    option_c= models.TextField(null=True, blank= True)
    option_d= models.TextField(null=True, blank= True)
    option_e= models.TextField(null=True, blank= True)

    def get_absolute_url(self):
        return reverse('home')

class Response(models.Model):
    name= models.CharField(max_length=35)
    survey= models.TextField()
    answer= models.TextField()

