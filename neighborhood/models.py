from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models import Q
import datetime as dt

class Neighborhood(models.Model):
    '''Displays the avalable neighborhoods in the area allowing users to choose the neighborhoods
        '''
    neighborhood_name = models.CharField(max_length=30)

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls,neighborhood_id):
        neighborhood = cls.objects.get(id=neighborhood_id)
        return neighborhood

    def update_neighborhood(self,name):
        self.name = name
        self.save()


    def __str__(self):
        return f'{self.neighborhood_name}'

class Profile(models.Model):
    '''Displays the user profile and allows the user to update it
        '''
    name =models.ForeignKey(User,on_delete=models.CASCADE)
    email = models.EmailField()
    contact = models.CharField(max_length=100)
    address =models.CharField(max_length=100)
    neighbourhood =models.ForeignKey(Neighborhood ,on_delete=models.CASCADE)

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
    neighbourhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)

    def create_business():
        self.save()

    def delete_business():
        self.delete()

    @classmethod
    def find_business(cls,search_term):
        businesses = cls.object.filter(business_name__icontains=search_term)
        return businesses


class Contact(models.Model):
    '''Displays the contact information for health services around police around the area
        '''
    title=models.CharField(max_length=75)
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=75)
    email=models.EmailField()
    contact=models.CharField(max_length=50)

    def create_contact():
        self.save()

    def delete_contact():
        self.delete()
    
    def __str__(self):
        return self.title


class Notification(models.Model):
    '''Displays notifications for the people n the neighbor hood
        '''
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=75)
    description=models.CharField(max_length=250)
    neighbourhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title




