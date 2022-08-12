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
    comment_002 = Comment.objects.get(id=random.randint(1,count))
    comment_003 = Comment.objects.get(id=random.randint(1,count))
    comment_004 = Comment.objects.get(id=random.randint(1,count))
    comment_005 = Comment.objects.get(id=random.randint(1,count))

    return render(
        request,
        'single_pages/comment_list.html',
        {
            'comment_001': comment_001,
            'comment_002': comment_002,
            'comment_003': comment_003,
            'comment_004': comment_004,
            'comment_005': comment_005,
        }
    )


'''
def today_word(request):
    comments = Comment.objects.all()

    count = 0 #comments 개수
    num_array = []

    for comment in comments:
        count += 1

    print(count)

    for i in range(0,5,1):
        num = random.randrange(1, count)
        num_array.append(num)

        print(num_array[i])

    comment_001 = Comment.objects.get(id=int(num_array[0]))
    comment_002 = Comment.objects.get(id=int(num_array[1]))
    comment_003 = Comment.objects.get(id=int(num_array[2]))
    comment_004 = Comment.objects.get(id=int(num_array[3]))
    comment_005 = Comment.objects.get(id=int(num_array[4]))

    return render(
        request,
        'single_pages/comment_list.html',
        {
            'comment_001': comment_001,
            'comment_002': comment_002,
            'comment_003': comment_003,
            'comment_004': comment_004,
            'comment_005': comment_005,
        }
    )
'''
