from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    ListView,
    DeleteView,
)

from .models import Article
from .forms import ArticleForm


class ArticleListView(ListView):
    queryset = Article.objects.all()
    template_name = 'articles/article_list.html'

class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'

    def get_object(self):
        article_id = self.kwargs.get('article_id')
        article_object = get_object_or_404(Article, id=article_id)

        if not article_object.active:
            raise Http404

        return article_object

class ArticleCreateView(CreateView):
    form_class = ArticleForm
    template_name = 'articles/article_form.html'
    queryset = Article.objects.all()


class ArticleUpdateView(UpdateView):
    form_class = ArticleForm
    template_name = 'articles/article_form.html'

    def get_object(self):
        article_id = self.kwargs.get('article_id')
        article_object = get_object_or_404(Article, id=article_id)

        if not article_object.active:
            raise Http404

        return article_object

class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'

    def get_object(self):
        article_id = self.kwargs.get('article_id')
        article_object = get_object_or_404(Article, id=article_id)

        if not article_object.active:
            raise Http404

        return article_object

    def get_success_url(self):
        return reverse('blog:index')
