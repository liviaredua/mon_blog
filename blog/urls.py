from django.urls import path

from blog.views import about, download, detail, news, tools

urlpatterns = [
    path('about/', about, name='about'),
    path('cv/', download),
    path('details/<int:idWK>', detail, name='detail'),
    path('news/', news, name='news'),
    path('', news, name='news'),
    path('tools/', tools, name='tools')
]