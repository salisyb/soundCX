from django.urls import path
from .views import apimain

urlpatterns = [
    path('', apimain)
]