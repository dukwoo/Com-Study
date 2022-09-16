from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView, CreateView

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


# def index(request):
#  return render(
#        request,
#        'diary/post_list.html',
#    )


class PostDetail(DetailView):
    model = Post


class PostUpdate(UpdateView):
    model = Post
    fields = ['content']

    template_name = 'diary/post_update_form.html'

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super(PostCreate,self).form_valid(form)
        else:
            return('/diary/')
