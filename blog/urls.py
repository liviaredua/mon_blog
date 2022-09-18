from xml.dom.minidom import Document
from django.urls import path
from blog.views import about, download, detail, news, tools, management, detailArt, Problema

urlpatterns = [
    path('about/', about, name='about'),
    path('management/', management, name='management'),
    path('cv/', download),
    path('details/<int:idWK>', detail, name='detail'),
    path('detailsArt/<int:idArt>', detailArt, name='detailArt'),
    path('news/', news, name='news'),
    #path('',  about, name='about'),
    path('',  Problema, name='problema'),
    path('tools/', tools, name='tools')
]