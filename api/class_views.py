from rest_framework.response import Response
from rest_framework.decorators import api_view
from blog.models import Category, Article
from .serializers import CategorySerializer, ArticleSerializer
from rest_framework import generics


class Categories(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer  # returns all the objects in the database


class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer  # returns a single model instances


# class CreateCategory(generics.CreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

class CreateCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# class UpdateCategory(generics.UpdateAPIView):  # this class does not put instances only empty form
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


class UpdateCategory(generics.UpdateAPIView):  # this class puts instances
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# class DeleteCategory(generics.DestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


class DeleteCategory(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UpdateANDDeleteArticle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# RECIPES
class Articles(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CreateArticle(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class UpdateArticle(generics.RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class DeleteArticle(generics.RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
