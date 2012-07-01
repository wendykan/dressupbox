from django.http import HttpResponse

# To implement more polls, see Part 3 of the official Django tutorial:
# https://docs.djangoproject.com/en/dev/intro/tutorial03/

def default(request):
    return HttpResponse("This is the default placeholder page.")

def login(request):
    return HttpResponse("This is the login page")

def signup(request):
    return HttpResponse("This is the signup page")

def map(request):
    return HttpResponse("This is the map page")

def dress(request):
    return HttpResponse("This is the map page")

def moreinfo(request):
    return HttpResponse("This is the more info page")