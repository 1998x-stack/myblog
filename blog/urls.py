from django.urls import path
from . import views


urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('article/add/', views.add_article, name='add_article'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('search/', views.search, name='search'),
    path('article/<int:pk>/comment/', views.add_comment, name='add_comment'),
]