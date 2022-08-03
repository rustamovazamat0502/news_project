from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Article, Category
from .forms import ArticleForm, LoginForm, RegistrationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib import messages


# def index(request):
#     articles = Article.objects.all()
#     result = '<h1>Hello world !!!</h1>'
#
#     for article in articles:
#         result += f'''<h2>Название: {article.title}</h2>
# <p>Описание: {article.content}<p>'''
#
#     return HttpResponse(result)

# def index(request):
#     articles = Article.objects.all()
#     content = {
#         'articles': articles,
#     }
#     return render(request, 'blog/all_articles.html', content)

class ArticleList(LoginRequiredMixin, ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'blog/all_articles.html'
    extra_context = {
        'title': 'All articles from class'
    }
    paginate_by = 3

    def get_queryset(self):
        return Article.objects.filter(is_published=True)


# def category_list(request, pk):
#     articles = Article.objects.filter(category_id=pk)
#     content = {
#         'articles': articles
#     }
#     return render(request, 'blog/all_articles.html', content)

class ArticleListByCategories(ArticleList):
    def get_queryset(self):
        return Article.objects.filter(
            category_id=self.kwargs['pk'], is_published=True
        ).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        category = Category.objects.get(pk=self.kwargs['pk'])
        context['title'] = category.title
        return context


# def article_details(request, pk):
#     article = Article.objects.get(pk=pk)
#
#     content = {
#         'article': article,
#         'title': article.title
#     }
#     return render(request, 'blog/details.html', content)

class ArticleDetail(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'blog/details.html'

    def get_queryset(self):
        return Article.objects.filter(pk=self.kwargs['pk'], is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        article = Article.objects.get(pk=self.kwargs['pk'])
        context['title'] = f'Статья: {article.title}'
        return context


# POST
# GET

# def add_article(request):
#     if request.method == 'POST':
#         form = ArticleForm(request.POST, request.FILES)
#         if form.is_valid():
#             article = Article.objects.create(**form.cleaned_data)
#             article.save()
#             return redirect('article_details', article.pk)
#     else:
#         form = ArticleForm()
#     context = {
#         'form': form,
#         'title': 'Добавить статью'
#     }
#     return render(request, 'blog/article_form.html', context)

class NewArticle(LoginRequiredMixin, CreateView):
    form_class = ArticleForm
    template_name = 'blog/article_form.html'
    extra_context = {
        'title': 'Добавить статью'
    }
    success_url = reverse_lazy('index')


class SearchView(ArticleList):
    def get_queryset(self):
        word = self.request.GET.get('q')
        article = Article.objects.filter(
            Q(title__icontains=word) | Q(content__icontains=word), is_published=True
        )
        total = article.count()
        messages.info(self.request, f"Search word: {word} ||| Total results: {total}")
        return article


class ArticleUpdate(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/article_form.html'


class ArticleDelete(LoginRequiredMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('index')
    context_object_name = 'article'


@login_required
def profile(request):
    return render(request, 'blog/profile.html', {
        'title': 'Ваш профиль'
    })


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, message='Вы успешно авторизовались')
            # return redirect("index")
            return redirect(request.GET['next'] if 'next' in request.GET else 'index')
        else:
            messages.error(request, 'Что то не так !!!')
            return redirect('login')
    else:
        form = LoginForm()

    context = {
        'title': 'Авторизация  пользователя',
        'form': form
    }

    return render(request, 'blog/user_login.html', context)


def user_logout(request):
    logout(request)
    messages.warning(request, message='Вы успешно вышли из аккаунта')
    return redirect('index')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Аккаунт успешно создан')
            next = request.POST.get('next', 'index')
            return redirect(next)
    else:
        form = RegistrationForm()
    context = {
        'title': 'Регистрация пользователя',
        'form': form
    }
    return render(request, 'blog/register.html', context)


@login_required
def about_us(request):
    return render(request, 'blog/about_us.html')


@login_required
def about_dev(request):
    return render(request, 'blog/about_dev.html')
