from django.urls import path
from . import views
from . import class_views

urlpatterns = [
    path("show_categories/", class_views.Categories.as_view(), name='show_categories'),
    path("category_detail/<int:pk>/", class_views.CategoryDetail.as_view(), name="category_detail"),
    path("create_category/", class_views.CreateCategory.as_view(), name='create_category'),
    path("category_update/<int:pk>/", class_views.UpdateCategory.as_view(), name="category_update"),
    path("category_delete/<int:pk>/", class_views.DeleteCategory.as_view(), name="delete_category"),
    path("update_delete_article/<int:pk>/", class_views.UpdateANDDeleteArticle.as_view(), name="update_delete"),

    path("show_articles/", class_views.Articles.as_view(), name='show_articles'),
    path("create_article/", class_views.CreateArticle.as_view(), name='create_article'),
    path("article_detail/<int:pk>/", class_views.ArticleDetail.as_view(), name='detail_article'),
    path("update_article/<int:pk>/", class_views.UpdateArticle.as_view(), name="update_article"),
    path("delete_article/<int:pk>/", class_views.DeleteArticle.as_view(), name="delete_article"),

]
