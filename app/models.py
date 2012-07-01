from django.db import models
import datetime
from PIL import Image

# Why __unicode__() instead of __str__()? See the Django tutorial for more info:
# https://docs.djangoproject.com/en/dev/intro/tutorial01/

class User(models.Model):
    """
    Represents users on DressUpBox.

    The user actually submits her location as a string, e.g., "New York" or "SF, CA."
    We take that location and convert it to a latitude and longitude pair with a Google
    Maps API call. We store it this way so that we can easily search by dress location.
    """
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __unicode__(self):
        return self.name

class Dress(models.Model):
    """Write a docstring for the Dress class."""
    owner = models.ForeignKey(User)
    brand = models.CharField(max_length=100)
    size = models.CharField(max_length=8)
    details = models.CharField(max_length=2000)
    color = models.CharField(max_length=50)
    image = models.ImageField(upload_to='dresses') # gets appended to MEDIA_ROOT
    style = models.CharField(max_length=100)
    occasion = models.CharField(max_length=100)

    def __unicode__(self):
        return self.brand + self.size

class Transaction(models.Model):
    """Write a docstring for the Transaction class."""
    owner = models.ForeignKey(User, related_name='transaction_owners')
    renter = models.ForeignKey(User, related_name='transaction_renters')
    date = models.DateTimeField('unspecified datetime')
    dress = models.ForeignKey(Dress)
