from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),
    path('create_post/',views.PostCreate.as_view()),
]
