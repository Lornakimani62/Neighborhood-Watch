from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models import Q
import datetime as dt


class Profile(models.Model):
    '''Displays the user profile and allows the user to update it
        '''
    name =models.ForeignKey(User,on_delete=models.CASCADE)
    email = models.EmailField()
    contact = models.CharField(max_length=100)
    address =models.CharField(max_length=100)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.name


class Business(models.Model):
    '''Displays the businesses around the given area
        '''
    business_name = models.CharField(max_length=100)
    email = models.EmailField()
    description = HTMLField()

    def create_business():
        self.save()

    def delete_business():
        self.delete()

    @classmethod
    def find_business(cls,search_term):
        businesses = cls.object.filter(business_name__icontains=search_term)
        return businesses
    

    

