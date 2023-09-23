from django.db import models

# Create your models here.
class register(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    FatherName = models.CharField(max_length=20)
    Address = models.CharField(max_length=20)
    Contact = models.CharField(max_length=20)
    MailId = models.CharField(max_length=20)
    Age = models.CharField(max_length=20)
    DOB = models.IntegerField(max_length=20)
    BloodGroup = models.CharField(max_length=20)
    Date = models.IntegerField(max_length=20)
    Gender = models.CharField(max_length=20)