from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatbot),
    path('chattrain',views.chattrain),
    path('chatanswer',views.chatanswer),
    path('make/',views.PostCreate.as_view()),
]