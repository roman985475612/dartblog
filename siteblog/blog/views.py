from django.db.models import F
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import get_object_or_404

from .models import Post, Category, Tag


class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 2
    extra_context = {
        'title': 'Classic Blog Design',
    }


class PostByCategory(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


class PostByTag(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Tag.objects.get(slug=self.kwargs['slug'])
        return context


class Search(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Результаты поиста: ' + self.request.GET.get('s')
        context['s'] = f"s={self.request.GET.get('s')}&"
        return context


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'

    def get_object(self):
        obj = super().get_object()
        obj.views = F('views') + 1
        obj.save()
        obj.refresh_from_db()
        return obj
