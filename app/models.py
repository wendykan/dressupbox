from django.db import models
import datetime
from PIL import Image

# Why __unicode__() instead of __str__()? See the Django tutorial for more info:
# https://docs.djangoproject.com/en/dev/intro/tutorial01/

class User(models.Model):
    """Write a docstring for the User class."""
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    # TODO: Facebook friends

    def __unicode__(self):
        return self.name

u = User(name = "Sharon Wong",
        email = "sharon.wong@gmail.com",
        latitude = "37",
        longitude = "30")

v = User(name = "Whit Cohen",
        email = "we.cohen@gmail.com",
        latitude = "37",
        longitude = "31")

v = User(name = "Michelle Sun",
        email = "michesun@gmail.com",
        latitude = "38",
        longitude = "30")


class Dress(models.Model):
    """Write a docstring for the Dress class."""
    owner = models.ForeignKey(User)
    brand = models.CharField(max_length=100)
    size = models.CharField(max_length=8)
    details = models.CharField(max_length=2000)
    color = models.CharField(max_length=50)
    # upload_to gets appended to MEDIA_ROOT
    image = models.ImageField(upload_to='dresses')
    style = models.CharField(max_length=100)
    occasion = models.CharField(max_length=100)

    def __unicode__(self):
        return self.brand + self.size

d = Dress(owner = u, 
        brand = ,
        size = ,
        details = ,
        color = ,
        image = ,
        style = ,
        occasion = )

class Transaction(models.Model):
    """Write a docstring for the Transaction class."""
    owner = models.ForeignKey(User, related_name='transaction_owners')
    renter = models.ForeignKey(User, related_name='transaction_renters')
    date = models.DateTimeField('unspecified datetime')
    dress = models.ForeignKey(Dress)