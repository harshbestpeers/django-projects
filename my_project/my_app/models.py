from django.db import models

# Create your models here.
class members(models.Model):
    firstname = models.CharField(max_length=225)
    lastname = models.CharField(max_length=225)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)


class user(models.Model):
    name = models.CharField(max_length=225)
    email = models.CharField(max_length=225)
    password = models.CharField(max_length=225)



