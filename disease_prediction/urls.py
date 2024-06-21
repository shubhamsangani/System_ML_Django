from django.contrib import admin
from django.urls import path
from disease_prediction import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("heart", views.heart, name='heart'),
    path("parkinsons", views.parkinsons, name='parkinsons'),
    path("diabetes", views.diabetes, name='diabetes'),
]
