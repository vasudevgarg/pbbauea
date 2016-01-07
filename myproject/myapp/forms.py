# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )

class SharedWith(forms.Form):
    shared_file=forms.CharField(label='Select a file for sharing',max_length=100)
    shared_user=forms.CharField(label='Select a user',max_length=100)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
