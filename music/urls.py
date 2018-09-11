from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# when boot up -> djagngotest -> settings.py -> look at INSTALLED_APPS -> MODELS (in this case)
# djangotest/urls.py --> music/urls.py
# each url is connected to one view to some html
app_name = 'music'
# IF UNABLE TO FIND; POSSIBLE SCENARIO: ADD AN "/" TO THE URL PATTERN
urlpatterns = [
    # /Bokeh/
    path("", views.IndexView.as_view(), name='index'),

    # /music/register/
    path("register/", views.UserFormView.as_view(), name='registration_html'),

    # /music/71/
    path("<int:pk>/", views.DetailView.as_view(), name='detail'),

    # /music/album/add/
    path("album/add/", views.AlbumCreate.as_view(), name = 'album-add'),

    # /music/album/2/
    path("album/<int:pk>/", views.AlbumUpdate.as_view(), name = 'album-update'),

    # /music/album/2/delete/
    path("album/<int:pk>/delete/", views.AlbumDelete.as_view(), name = 'album-delete')



]