from django.urls import path
from .views import Search_The_Image,Scrapp_Image,GetImage

urlpatterns = [
    path('searchimage/' ,Search_The_Image),
    path('scrapimage/' ,Scrapp_Image),
    path('download/<str:imgname>/' ,GetImage),
]