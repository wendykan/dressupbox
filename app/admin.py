from django.contrib import admin

from app.models import User
from app.models import Dress
from app.models import Transaction

admin.site.register(User)
admin.site.register(Dress)
admin.site.register(Transaction)

# Not going to bother implementing more complicated admin tools right now
# For more info, go to Page 2 of the official Django tutorial
# https://docs.djangoproject.com/en/dev/intro/tutorial02/