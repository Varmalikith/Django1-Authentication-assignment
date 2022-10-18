from enum import auto
from django.db import models

class Studentresults(models.Model):
    username = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)  
    lname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    pass1 = models.CharField(max_length=10)
    pass2 = models.CharField(max_length=10)
    specialiazation = models.CharField(max_length=100)
    address = models.TextField()
    
