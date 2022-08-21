from django.shortcuts import render
from django.views.generic import DetailView
from .models import Comment
import random

def today_word(request):
    comments = Comment.objects.all()

    count = 0
    for comment in comments:
        count += 1
        
    #랜덤 글귀 뜨도록 설정
    comment_001 = Comment.objects.get(id=random.randint(1,count))

    return render(
        request,
        'single_pages/comment_list.html',
        {
            'comment_001': comment_001,
        }
    )


def landing(request):

    return render(
        request,
        'single_pages/landing.html',
    )
