from django.urls import path
from . import views

urlpatterns = [
    path('phrase/', views.phrase),
]