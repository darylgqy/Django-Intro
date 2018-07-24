from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1> Music App Homepage</h1>')

def detail(request, album_id):
    return HttpResponse("<h2>details for album_id: " + str(album_id) + '</h2>')



