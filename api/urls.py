from django.urls import path
from . import views
from . import class_views

urlpatterns = [
    path("show_categories/", views.show_categories, name='show_categories'),
    path("create_category/", views.create_category, name='create_category'),
    path("category_detail/<int:pk>/", views.category_detail, name="category_detail"),
    path("category_update/<int:pk>/", views.update_category, name="category_update"),
    path("category_delete/<int:pk>/", views.delete_category, name="delete_category"),

    path("show_articles/", views.show_articles, name='show_articles'),
    path("create_article/", views.create_article, name='create_article'),
    path("article_detail/<int:pk>/", views.article_detail, name='detail_article'),
    path("update_article/<int:pk>/", views.update_article, name="update_article"),
    path("delete_article/<int:pk>/", views.delete_article, name="delete_article"),

]
