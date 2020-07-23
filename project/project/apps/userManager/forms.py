from django import forms
from django.forms import ModelForm
from .models import Profile, Assignment
from django.contrib.auth.models import User


class FileForm(ModelForm):
    class Meta:
        model = Assignment
        fields = ['file_teacher', 'file_student']

    def __init__(self, *args, **kwargs):
        super(FileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class CreateAccountForm(ModelForm):
    password2 = forms.CharField(widget=forms.TextInput(attrs={'required':
                                                              True}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'required':
                                                                 True}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'username', 'password']

    def __init__(self, *args, **kwargs):
        super(CreateAccountForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class LoginForm(forms.Form):
    username = forms.CharField(label='نام کاربری', max_length=100)
    password = forms.CharField(label='کلمه عبور',
                               max_length=32, widget=forms.PasswordInput)

    username.widget.attrs.update({'class': 'form-control'})
    password.widget.attrs.update({'class': 'form-control'})
