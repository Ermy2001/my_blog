from django.shortcuts import render, get_object_or_404
from account.models import User
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from django.http import HttpResponse, JsonResponse, Http404
from .models import Article, Category
# Create your views here.


# def home(request, page=1):
#     article_list = Article.objects.published()
#     p = Paginator(article_list, 2)
#     #page_n = request.GET.get('page')
#     articles = p.get_page(page)
#     context = {
#         "articles": articles
#     }
#     return render(request, "blog/article_list.html", context)
class ArticleList(ListView):
    # model = Article
    # template_name = "blog/article_list.html"
    # context_object_name = "articles"
    queryset = Article.objects.published()
    paginate_by = 2


# def detail(request, slug):
#     context = {
#         "article": get_object_or_404(Article, slug=slug, status="p")  # or(Article.objects.published, slug=slug)
#     }
#     return render(request, "blog/article_detail.html", context)
class ArticleDetail(DetailView):
    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article, slug=slug, status="p")


# def category(request, slug, page=1):
#     category = get_object_or_404(Category, slug=slug, status=True)
#     article_list = category.article_s.published()
#     p = Paginator(article_list, 2)
#     articles = p.get_page(page)
#     context = {
#         "category": category,
#         "articles": articles
#     }
#     return render(request, "blog/list.html", context)

class CategoryList(ListView):
    paginate_by = 2
    template_name = 'blog/category_list.html'

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active(), slug=slug)
        return category.article_s.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = category
        return context


class AuthorList(ListView):
    paginate_by = 2
    template_name = 'blog/author_list.html'

    def get_queryset(self):
        global author
        username = self.kwargs.get('username')
        author = get_object_or_404(User, username=username)
        return author.article_s.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["author"] = author
        return context


