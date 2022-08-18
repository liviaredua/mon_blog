from django.urls import path

from blog.views import about, download, detail, news, tools

urlpatterns = [
    path('', about, name='about'),
    path('cv/', download),
    path('details/', detail, name='detail'),
    path('news/', news, name='news'),
    path('tools/', tools, name='tools')
]