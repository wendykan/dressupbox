from django.shortcuts import render_to_response
from app.models import User, Dress, Transaction
from django.http import HttpResponse

# To implement more views, see Part 3 of the official Django tutorial:
# https://docs.djangoproject.com/en/dev/intro/tutorial03/

# Dynamic pages

def search(request):
    return render_to_response('frontend/need.html')

def results(request):
    # Even though we claim this is a search response, this is actually all dresses.
    # We know that. We just haven't implemented search yet.
    all_dresses = Dress.objects.all()
    return render_to_response('frontend/results.html', {'all_dresses': all_dresses})

# Static pages

def default(request):
    return HttpResponse("Hello, world. You're at the app index.")

def login(request):
    return HttpResponse("This is the login page")

def signup(request):
    return HttpResponse("This is the signup page")

def map(request):
    return HttpResponse("This is the map page")

def dress(request, dress_id):
#    return HttpResponse("You're looking at the dress id %s." % dress_id)
    dress = Dress.objects.get(id=dress_id)
    return render_to_response('frontend/dress.html', {'dress':dress})

def moreinfo(request):
    return HttpResponse("This is the more info page")