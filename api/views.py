from rest_framework.response import Response
from rest_framework.decorators import api_view
from blog.models import Category, Article
from .serializers import CategorySerializer, ArticleSerializer
from django.shortcuts import get_object_or_404, get_list_or_404


# ============================================================================
# CATEGORIES
# ============================================================================
@api_view(['GET'])
def show_categories(request):
    categories = get_list_or_404(Category)
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def create_category(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        serializer = CategorySerializer()
    return Response(serializer.data)


@api_view(['GET'])
def category_detail(request, pk):
    category = get_object_or_404(Category, id=pk)
    serializer = CategorySerializer(category, many=False)
    return Response(serializer.data)


@api_view(["GET", "PUT", "PATCH"])
def update_category(request, pk):
    category = get_object_or_404(Category, id=pk)
    serializer = CategorySerializer(instance=category, data=request.data, many=False)
    if serializer.is_valid():
        serializer.save()
    else:
        serializer = CategorySerializer(instance=category, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_category(request, pk):
    category = get_object_or_404(Category, id=pk)
    if request.method == "DELETE":
        category.delete()
    return Response("Category Deleted Successfully !!!")


# ============================================================================
# ARTICLES
# ============================================================================
@api_view(['GET'])
def show_articles(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_article(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def update_article(request, pk):
    article = Article.objects.get(id=pk)
    serializer = ArticleSerializer(instance=article, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def article_detail(request, pk):
    article = Article.objects.get(id=pk)
    serializer = ArticleSerializer(article, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_article(request, pk):
    article = Article.objects.get(id=pk)
    article.delete()
    return Response("Article Deleted Successfully !!!")
