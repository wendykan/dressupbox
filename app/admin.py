from django.contrib import admin

from app.models import User
from app.models import Dress
from app.models import Transaction

admin.site.register(User)
admin.site.register(Dress)
admin.site.register(Transaction)