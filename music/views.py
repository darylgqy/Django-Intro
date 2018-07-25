from django.shortcuts import render, get_object_or_404
from .models import Album


def index(request):
    # stores all albums in database into all_albums
    all_albums = Album.objects.all()
    # django already set up to look into a template dir (if u create or it exists)
    context = {'all_albums': all_albums, }
    # render shortcuts via integrating httpresponse into it
    return render(request, 'music/index.html', context)


def detail(request, album_id):
    # try:
    #     album = Album.objects.get(pk=album_id)
    # except Album.DoesNotExist:
    #     raise Http404("Album does not exist")
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album, })
