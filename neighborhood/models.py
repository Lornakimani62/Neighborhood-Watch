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


