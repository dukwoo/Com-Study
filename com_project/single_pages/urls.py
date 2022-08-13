from django.urls import path
from . import views

urlpatterns = [
    path('today_word/', views.today_word),
    path('',views.landing),
]