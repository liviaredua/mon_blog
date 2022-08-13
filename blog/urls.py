from django.urls import path

from blog.views import about, download

urlpatterns = [
    path('', about),
    path('cv/', download)
]