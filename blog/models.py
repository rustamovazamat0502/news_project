from django.db import models
from django.urls import reverse

class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')

    def get_absolute_url(self):
        return reverse('category_list', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __repr__(self):
        return f'Category(pk={self.pk}, title="{self.title}")'

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    content = models.TextField(blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    photo = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано ли')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('article_details', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'Article(pk={self.pk}, title="{self.title}")'


