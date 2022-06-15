from django.test import TestCase
from django.contrib.auth.models import User
from .models import Projects, Comments, Profile, Votes
import datetime

# Create your tests here.


class Projects(TestCase):
    def setUp(self):
        self.name = Projects(name='instagram-clone')
        self.user = Projects(user='kevin')
        self.description = Projects(description='This is a Description')
        self.link = Projects(link='https://insta-apk.herokuapp.com/')
        self.date = Projects(date='reading')

    def test_string(self):
        self.assertEqual(str(self.name), 'instagram-clone')

    def test_string(self):
        self.assertEqual(str(self.user), 'kevin')

    def test_string(self):
        self.assertEqual(str(self.description), 'This is a Description')

    def test_string(self):
        self.assertEqual(str(self.link), 'https://insta-apk.herokuapp.com/')

    def test_string(self):
        self.assertEqual(str(self.date), '2022,01,10')    


class Profile(TestCase):
    def setUp(self):
        self.user = Profile(user='kevin')
        self.bio = Profile(bio='This is my bio')

    def test_string(self):
        self.assertEqual(str(self.user), 'kevin')

    def test_string(self):
        self.assertEqual(str(self.bio), 'This is my bio')


class Votes(TestCase):
    def setUp(self):
        self.username = Profile(username='kevin')
        self.bio = Profile(bio='this is my bio')

    def test_string(self):
        self.assertEqual(str(self.bio), 'this is my bio')

    def test_string(self):
        self.assertEqual(str(self.username), 'kevin')


class Comments(TestCase):
    def setUp(self):
        self.user = Comments(user='kevin')
        self.comment = Comments(comment='this is a comment')
        self.pro_id = Comments(pro_id='1')

    def test_string(self):
        self.assertEqual(str(self.user), 'kevin')

    def test_string(self):
        self.assertEqual(str(self.comment), 'this is a comment')
