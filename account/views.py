from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . mixin import FieldsMixin, FormValidMixin, AuthorAccessMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView
from blog.models import Article

# Create your views here.


class ArticleList(LoginRequiredMixin, ListView):
    # queryset = Article.objects.all()
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        else:
            return Article.objects.filter(author=self.request.user)
    template_name = "registration/home.html"


class ArticleCreate(LoginRequiredMixin, FieldsMixin, FormValidMixin, CreateView):
    model = Article
    template_name = "registration/article-create-update.html"


class ArticleUpdate(AuthorAccessMixin, FieldsMixin, FormValidMixin, UpdateView):
    model = Article
    template_name = "registration/article-create-update.html"


