from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm

User = get_user_model()


class CreationForm(UserCreationForm):
    username = forms.CharField(max_length=191,
                               label='Имя пользователя',
                               widget=forms.TextInput({
                                       "placeholder": "nickname"}))
    first_name = forms.CharField(label='Имя', max_length=200,
                                 widget=forms.TextInput(
                                        {"placeholder": "Василий"}
                                                        )
                                 )
    email = forms.EmailField(required=True,
                             max_length=200,
                             label='Email',
                             widget=forms.TextInput({
                                  "placeholder": "vasiliy@mail.ru"}))
    password1 = forms.CharField(widget=forms.PasswordInput(
                                attrs={'class': 'form-control',
                                       'type': 'password',
                                       'name': 'password',
                                       'placeholder': 'Ваш пароль'}),
                                label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput(
                                attrs={'class': 'form-control',
                                       'type': 'password',
                                       'name': 'password',
                                       'placeholder': 'Ещё раз'}),
                                label='Повторите пароль')

    class Meta(UserCreationForm.Meta):
        model = User
        ields = ('first_name', 'username', 'email', 'password1', 'password2')


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(
                                   attrs={'class': 'form-control',
                                          'type': 'password',
                                          'name': 'old_password'}),
                                   label='Старый пароль')
    new_password1 = forms.CharField(widget=forms.PasswordInput(
                                    attrs={'class': 'form-control',
                                           'type': 'password',
                                           'name': 'new_password1'}),
                                    label='Новый пароль')

    new_password2 = forms.CharField(widget=forms.PasswordInput(
                                    attrs={'class': 'form-control',
                                           'type': 'password',
                                           'name': 'new_password2'}),
                                    label='Повторите новый пароль')

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
