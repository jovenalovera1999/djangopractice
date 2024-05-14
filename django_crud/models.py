from django.db import models

# Create your models here.

class Gender(models.Model):
    gender_id = models.BigAutoField(primary_key=True)
    gender = models.CharField(max_length=55, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'genders'

    def __str__(self):
        return self.gender

class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=55)
    middle_name = models.CharField(max_length=55, blank=True)
    last_name = models.CharField(max_length=55)
    age = models.IntegerField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    birthdate = models.DateField()
    username = models.CharField(max_length=55, unique=True)
    password = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'