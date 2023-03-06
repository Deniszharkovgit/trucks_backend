from django.urls import path
from trucks import views

urlpatterns = [
    path('trucks', views.trucks_page),
]
