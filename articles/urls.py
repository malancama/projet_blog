from django.urls import path
from .views import list_article, ajout_article, modifier, article_detail, delete_article, add_comment
urlpatterns = [
    path('', list_article, name='list_articles'),
    path('ajout', ajout_article, name='ajout_article'),
    path('modifier/<int:id>/', modifier, name='modifier_article'),
    path('article_detail/<int:id>/', article_detail, name='article_detail'),
    path('delete_article/<int:id>/', delete_article, name='delete_article'),
    path('add_comment/<int:id>/', add_comment, name='add_comment')
]