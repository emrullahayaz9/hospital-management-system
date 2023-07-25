from django.db import models

# Create your models here.
class PatienceInformation(models.Model):
    name= models.CharField(max_length=100, unique=True)
    surname= models.CharField(max_length=100)
    disease_type= models.CharField(max_length=100)
    drugs= models.CharField(max_length=100)
