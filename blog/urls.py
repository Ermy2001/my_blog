from django.urls import path
from .views import ArticleList, ArticleDetail, CategoryList, AuthorList


app_name = 'blog'
urlpatterns = [
    path('', ArticleList.as_view(), name='home'),
    path('page/<int:page>', ArticleList.as_view(), name='home'),
    path('post/<slug:slug>', ArticleDetail.as_view(), name='detail'),
    path('category/<slug:slug>', CategoryList.as_view(), name='categori'),
    path('category/<slug:slug>/page/<int:page>', CategoryList.as_view(), name='categori'),
    path('category/<slug:username>', AuthorList.as_view(), name='author'),
    path('category/<slug:username>/page/<int:page>', AuthorList.as_view(), name='author')
]
