from django.urls import path

from .views import (
    ArticleCreateView,
    ArticleDeleteView,
    ArticleDetailView,
    ArticleListView,
    ArticleUpdateView
)

app_name = 'blog'

urlpatterns = [
    path('', ArticleListView.as_view(), name='index'),
    path('<int:article_id>', ArticleDetailView.as_view(), name='article_detail'),
    path('add/', ArticleCreateView.as_view(), name='article_create'),
    path('<int:article_id>/update', ArticleUpdateView.as_view(), name='article_update'),
    path('<int:article_id>/delete', ArticleDeleteView.as_view(), name='article_delete'),
]
