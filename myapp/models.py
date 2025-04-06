from django.db import models
from djongo import models  #Djongo allows using MongoDB with Django ORM
from django.contrib.auth.hashers import make_password, check_password

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)  #Ensure unique usernames
    password = models.CharField(max_length=255)  #Store hashed passwords

    def save(self, *args, **kwargs):
        
        #Overrides the save method to hash the password before storing it in MongoDB.
        self.password = make_password(self.password)  #Hash password before saving
        super().save(*args, **kwargs) #calls the parent save method

    def check_password(self, raw_password):
        #Checks the hashed password against user input.
        return check_password(raw_password, self.password)

    class Meta:
        db_table = "users"  #The collection name in MongoDB
        

