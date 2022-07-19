from django import forms
from django.forms.widgets import Textarea
from .models import Comment

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=Textarea())


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name', 'tabindex': 1}),
            'email': forms.TextInput(attrs={'placeholder': 'Email', 'tabindex': 2}),
            'body': forms.Textarea(attrs={'placeholder': 'Enter message...', 'tabindex': 3}),
        }


class SearchForm(forms.Form):
    query = forms.CharField()
