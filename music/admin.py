from django.contrib import admin
from .models import Album, Song
#register Album class at admin site
admin.site.register(Album)
admin.site.register(Song)
