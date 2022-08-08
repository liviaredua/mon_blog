from django.urls import path

from blog.views import about

urlpatterns = [
    path('', about),
]