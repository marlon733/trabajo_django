from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField( null=True)
  joined_date = models.DateField(null=True)
  gmail = models.EmailField(max_length=100, null=True)
  genero = models.CharField (max_length=100,null=True)
  edad= models.IntegerField(max_length=3, null=True)