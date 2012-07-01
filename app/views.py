from django.shortcuts import render_to_response
from app.models import User, Dress, Transaction
from django.http import HttpResponse
#from app.google_map_connect import google_map

# To implement more views, see Part 3 of the official Django tutorial:
# https://docs.djangoproject.com/en/dev/intro/tutorial03/

# Dynamic pages

def search(request):
    return render_to_response('frontend/need.html')

def search_results(request):
    
    print('this is search_results method')
    location_text = request.GET.get('location')
    [lat, lng] = get_coordinate(location_text)
    print [lat, lng]
    
    nearby_dresses = []
    
    all_dresses = Dress.objects.all()
    for dress in all_dresses:
    	user = dress.owner
        dist = distance_on_unit_sphere(lat, lng, user.latitude, user.longitude)
        if dist < float(request.GET.get('distance')):
        	print dist
        	print request.GET.get('distance')
        	nearby_dresses.append(dress)
        
    return render_to_response('frontend/search_results.html', {'location_text': location_text, 'nearby_dresses': nearby_dresses} )

      

def results(request):
    # Even though we claim this is a search response, this is actually all dresses.
    # We know that. We just haven't implemented search yet.
    all_dresses = Dress.objects.all()
    return render_to_response('frontend/results.html', {'all_dresses': all_dresses})

# Static pages

def default(request):
    return HttpResponse("Hello, world. You're at the app index.")

def home(request):
    return render_to_response('frontend/home.html')

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
    
    
    
    
import urllib, json
import pprint
import re

def get_coordinate(address):

  URL = "http://maps.googleapis.com/maps/api/geocode/json?address="
    #address = "1881+Sutter+St,+San+Francisco,+CA"
    #address = "1881 Sutter St, San Francisco, CA"
    #address = "Chicago"
  address = address.replace(' ','+')
  URL2 = URL+address+"&sensor=false"
  googleResponse = urllib.urlopen(URL2)
  jsonResponse = json.loads(googleResponse.read())
    #pprint.pprint(jsonResponse)
  lat = json.dumps([s['geometry']['location']['lat'] for s in jsonResponse['results']])
  lng = json.dumps([s['geometry']['location']['lng'] for s in jsonResponse['results']])
  lat = lat.replace('[','')
  lat = lat.replace(']','')
  lng = lng.replace('[','')
  lng = lng.replace(']','')
    #    print(float(lat))
    #    print(float(lng))

  return [float(lat), float(lng)]    
  
import math

def distance_on_unit_sphere(lat1, long1, lat2, long2):

    # Convert latitude and longitude to 
    # spherical coordinates in radians.
    degrees_to_radians = math.pi/180.0
        
    # phi = 90 - latitude
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians
        
    # theta = longitude
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians
        
    # Compute spherical distance from spherical coordinates.
        
    # For two locations in spherical coordinates 
    # (1, theta, phi) and (1, theta, phi)
    # cosine( arc length ) = 
    #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
    # distance = rho * arc length
    
    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
           math.cos(phi1)*math.cos(phi2))
    arc = math.acos( cos )

    # Remember to multiply arc by the radius of the earth 
    # in your favorite set of units to get length.
    return arc*3963  