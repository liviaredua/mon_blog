from django.urls import path

from blog.views import about, download, detail

urlpatterns = [
    path('', about, name='about'),
    path('cv/', download),
    path('details/', detail, name='detail')
]