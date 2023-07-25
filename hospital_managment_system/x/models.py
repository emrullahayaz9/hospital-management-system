from django.db import models
from django.forms import ModelForm

class UsersModel(models.Model):
    choices = (('D','Doctor'),
               ('P', 'Patience'))
    username=models.CharField(max_length=100, null=False, unique=True)
    password=models.CharField(max_length=100, null=False)
    role=models.CharField(max_length=1, choices=choices, null=False)

class UsersForm(ModelForm):
   class Meta:
      model = UsersModel
      fields= '__all__'

   
 
