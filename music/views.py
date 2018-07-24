from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Album


def index(request):
    # stores all albums in database into all_albums
    # returns the html version of all albums
    all_albums = Album.objects.all()
    html = ''
    for album in all_albums:
        url = "/music/" + str(album.id) + "/"
        html += '<a href="' + url + '">' + album.album_title + '</a><br>'
    return HttpResponse(html)


def detail(request, album_id):
    return HttpResponse("<h2>details for album_id: " + str(album_id) +"</h2>")
