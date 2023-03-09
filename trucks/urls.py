from django.urls import path
from trucks import views
from trucks.views import MainView

urlpatterns = [
    path('trucks', MainView.as_view()),
]
