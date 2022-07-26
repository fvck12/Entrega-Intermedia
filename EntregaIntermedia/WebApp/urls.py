from django.urls import path

from WebApp.views import inicio, about, post, contact

urlpatterns = [
    path('', inicio, name="inicio"),
    path('about', about, name="about"),
    path('post', post, name="post"),
    path('contact', contact, name="contact"),
]