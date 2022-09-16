from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatbot),
    path('chattrain',views.chattrain),
    path('chatanswer',views.chatanswer),
]