from django.urls import path
from .views import *

urlpatterns = [
    # path('', index, name='index'),
    path('', ArticleList.as_view(), name='index'),
    # path('category/<int:pk>/', category_list, name='category_list'),
    path('category/<int:pk>/', ArticleListByCategories.as_view(), name='category_list'),
    # path('article/<int:pk>', article_details, name='article_details'),
    path('article/<int:pk>', ArticleDetail.as_view(), name='article_details'),
    # path('new/', add_article, name='add_article')
    path('new/', NewArticle.as_view(), name='add_article'),
    path('search/', SearchView.as_view(), name='search_results'),
    # path('search/', search_func, name='search_results'),
    path('article/<int:pk>/update', ArticleUpdate.as_view(), name='article_update'),
    path('article/<int:pk>/delete', ArticleDelete.as_view(), name='article_delete'),
    path('profile/', profile, name='profile'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('about_us/', about_us, name='about_us'),
    path('about_dev/', about_dev, name='about_dev')
]
