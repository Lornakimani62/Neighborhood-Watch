from django.test import TestCase
from django.contrib.auth.models import User
from .models import *

class NeighborhoodTestClass(TestCase):
    def setUp(self):
        self.new_neighborhood = Neighborhood(id=1,neighborhood_name='Test Neighborhood')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_neighborhood,Neighborhood))

    def test_create_neighborhood(self):
        self.new_neighborhood.create_neighborhood()
        neighborhoods = Neighborhood.objects.all()
        self.assertTrue(len(neighborhoods) > 0)


class BusinessTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='user',password='user-password')
        self.new_neighborhood = Neighborhood(id=1,neighborhood_name='Test Neighborhood')
        self.new_neighborhood.save()
        self.new_business = Business(id = 1,name='Test Business',owner=self.new_user,business_location='Test Location',business_neighborhood=self.new_neighborhood,email='business@email.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_business,Business))

    def test_create_business(self):
        self.new_business.create_business()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) > 0)

    def test_delete_business(self):
        self.new_business.delete_business()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) == 0)

    def test_find_business(self):
        self.new_business.create_business()
        business = Business.find_business(1)
        self.assertEqual(business.name,'Test Business')

