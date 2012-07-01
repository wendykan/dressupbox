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

'''u1 = User(name = "Sharon Wong",
        email = "sharon.wong@gmail.com",
        latitude = "37",
        longitude = "30")

u2 = User(name = "Whit Cohen",
        email = "we.cohen@gmail.com",
        latitude = "37",
        longitude = "31")

u3 = User(name = "Michelle Sun",
        email = "michesun@gmail.com",
        latitude = "38",
        longitude = "30")

u4 = User(name = "Ashley Lorden",
        email = "ashley.f.lorden@gmail.com",
        latitude = "37",
        longitude = "31")

u5 = User(name = "Wendy Kan",
        email = "wendykan@gmail.com",
        latitude = "37",
        longitude = "30")
'''
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
'''
u1_d1 = Dress(owner = u1,
    size = 'M',
    brand = 'Herve Ledger'
    details = 'Knee length, figure hugging and sexy',
    color = 'black',
    image = '/imgs/herveledger_black.png'
    style = 'Sleeveless',
    occasion = 'Evening' )

u1_d2 = Dress(owner = u1,
        size = 'M',
        brand = 'Free People'
        details = 'Casual and cute. Perfect for picnic and day out!',
        color = 'White',
        image = '/imgs/free_people_black.png',
        style = 'Mini',
        occasion = 'Day')

u1_d3 = Dress(owner = u1,
        size = 'M',
        brand = 'J Crew'
        details = 'Sleek and slim cut, formal for work',
        color = 'Black',
        image = '/imgs/j_crew_black.png',
        style = 'Knee length',
        occasion = 'Business casual')

u2_d1 = Dress(owner = u2,
        size = 'XS',
        brand = 'DvF'
        details = 'Beach dress, vacation and cruising',
        color = 'orange',
        image = '/imgs/dvf_orange.png'
        style = 'Cap',
        occasion = 'Beach' )

u2_d2 = Dress(owner = u2,
        size = 'XS',
        brand = 'BCBG'
        details = 'Can wear for cocktails and night-out. Also great for wedding reception!',
        color = 'White',
        image = '/imgs/BCBG_tube_white_blue.png',
        style = 'Strapless',
        occasion = 'Wedding')

u2_d3 = Dress(owner = u2,
        size = 'M',
        brand = 'Rag and Bone'
        details = 'Raglan seams detail the shoulders of a languid tank dress with a shoulder-baring back and cool, heathered finish',
        color = 'Grey',
        image = '/imgs/rag_bone_grey.png',
        style = 'Knee length',
        occasion = 'Day')

u3_d1 = Dress(owner = u3,
        size = 'S',
        brand = 'Lulus'
        details = 'With a sexy open back and a line of fabric-covered buttons, the Take Me Back Cutout Peach Dress is exactly where you will want to be! A feminine sleeveless bodice with princess seams meets a delightfully full circle skirt at the banded waistline.',
        color = 'orange',
        image = '/imgs/takemeback_peach.png'
        style = 'mini',
        occasion = 'Girls night out' )

u3_d2 = Dress(owner = u3,
        size = 'S',
        brand = 'Forever 21'
        details = 'Light, ventilating qualities of maxi dresses, who can resist? Treat yourself a fashionable picnic this summer!',
        color = 'White',
        image = '/imgs/forever21_floral.png',
        style = 'maxi',
        occasion = 'Picnic')

u3_d3 = Dress(owner = u3,
        size = 'S',
        brand = 'Rebecca Taylor'
        details = 'Wow your date with beige sweetness!',
        color = 'Beige',
        image = '/imgs/chanel_beige.png',
        style = 'Mini',
        occasion = 'Date')

u3_d4 = Dress(owner = u3,
        size = 'S',
        brand = 'Tibi'
        details = 'Savor the attention on you on your night out with this Tibi red dress!',
        color = 'Red',
        image = '/imgs/tibi_red.png',
        style = 'Knee length',
        occasion = 'Day')
###DONE above##
u4_d1 = Dress(owner = u4,
        size = 'XS',
        brand = 'Express'
        details = 'What is better way to hit the Friday night festivities than with this playful gold dress? ',
        color = 'Gold',
        image = '/imgs/Express_Sparkle.png',
        style = 'knee length',
        occasion = 'Evening')

u4_d2 = Dress(owner = u4,
        size = 'XS',
        brand = 'Alice + Olivia'
        details = 'Lavish yourself with attention with this gorgeous red dress.',
        color = 'Red',
        image = '/imgs/AliciaNOlivia_red.png',
        style = 'Strapless',
        occasion = 'Girls night out')

u4_d3 = Dress(owner = u4,
        size = 'XS',
        brand = 'TWELFTH STREET BY CYNTHIA VINCENT'
        details = 'Enjoy your date night with this fun black tube with flowy details. ',
        color = 'Black',
        image = '/imgs/12th_black.png',
        style = 'Strapless',
        occasion = 'Date')
'''

class Transaction(models.Model):
    """Write a docstring for the Transaction class."""
    owner = models.ForeignKey(User, related_name='transaction_owners')
    renter = models.ForeignKey(User, related_name='transaction_renters')
    date = models.DateTimeField('unspecified datetime')
    dress = models.ForeignKey(Dress)