from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput
from .models import URLs


class AddLinkForm(forms.ModelForm):

    class Meta:
        model = URLs
        fields = ('name', 'short_name')

        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'links__field first'
                }
            ),
            'short_name': TextInput(
                attrs={
                    'class': 'links__field'
                }
            ),
        }

class UserRegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        del self.fields['password2']

    username = forms.SlugField(label='Имя пользователя')
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'registration__email'}
        )
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'password1']


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(
        label='Введите новый логин',
        required=True,
        help_text='Обязательное поле. Только буквы, цифры и символы @/./+/-/_',
        widget=forms.TextInput(attrs={'class': 'profile__change'})
    )

    email = forms.EmailField(
        required=True,
        label='Введите новый Email',
        widget=forms.TextInput(attrs={'class': 'profile__change'})
    )

    class Meta:
        model = User
        fields = ['username', 'email']


