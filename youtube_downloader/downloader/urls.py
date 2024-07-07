from django.urls import path
from .views import download,home

urlpatterns = [
    path('', home, name='home'),
    path('download/', download, name='download'),
]
