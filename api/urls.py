from django.urls import path
from . import views

urlpatterns = [
    path("show_categories/", views.show_categories, name='show_categories'),
    path("create_category/", views.create_category, name='create_category'),
    path("category_detail/<int:pk>/", views.category_detail, name="category_detail"),
    path("category_update/<int:pk>/", views.update_category, name="category_update"),
    path("category_delete/<int:pk>/", views.delete_category, name="delete_category"),

    path("show_articles/", views.show_articles, name='show_articles'),
    path("create_article/", views.create_article, name='create_article'),
    path("article_detail/<int:pk>/", views.article_detail, name='article_detail'),
    path("article_update/<int:pk>/", views.update_article, name="article_update"),
    path("article_delete/<int:pk>/", views.delete_article, name="delete_article"),

]
