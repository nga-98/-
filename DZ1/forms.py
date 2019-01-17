from django import forms
from .models import Post, Picture


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title', 'text')


class PictureForm(forms.ModelForm):
    class Meta:
        model=Picture
        fields=('name', 'picture')
