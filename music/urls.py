from django.urls import path
from . import views
# IF UNABLE TO FIND; POSSIBLE SCENARIO: ADD AN "/" TO THE URL PATTERN
urlpatterns = [
    # /music/
    path("", views.index, name='index'),

    # /music/71/
    path("<int:album_id>/", views.detail, name='detail'),
]