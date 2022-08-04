from django import forms
from django.contrib.auth.models import User

from .models import Article
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'photo',
            'is_published',
            'category'
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Название',
                'class': 'form-control'
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Описание',
                'class': 'form-control'
            }),
            'is_published': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            })
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', help_text="max 20202020",
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=30, help_text='Максимум 30 символов',
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'
                               }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Подтвердите пароль'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Почта'
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
