from django.urls import path
from .views import home_page, about_page

urlpatterns = [
    path("", home_page, name="home"),
    path("Sobre/", about_page, name="about"),
]
