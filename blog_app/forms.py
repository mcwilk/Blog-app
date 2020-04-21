from django import forms
from .models import Post

class PostSheet(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'text']