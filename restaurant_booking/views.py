from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def the_restaurant_booking(request):
    return HttpResponse("Book Table")
