from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView

from . import models
from .models import Post
from django.core.paginator import Paginator


class PostList(ListView):
    model = Post
    ordering = '-pk'
    template_name = 'diary/post_list.html'
    paginate_by = 9


#def post_list(request):
#    posts_all = Post.objects.all()
#    paginator = Paginator(posts_all, 9)
#    page = request.GET.get('page')
#    posts = paginator.get_page(page)

#    return render(request, 'post_list.html', {'posts': posts})


class PostDetail(DetailView):
    model = Post


class PostUpdate(UpdateView):
    model = Post
    fields = ['content']

    template_name = 'diary/post_update_form.html'
