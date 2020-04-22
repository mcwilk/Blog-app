from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment

class PostSheet(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'text']

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text',]
        labels = {'text': 'Comment here:'}
        
