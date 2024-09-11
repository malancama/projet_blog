from django import forms
from .models import Article, Comment


class Article_from(forms.ModelForm):
    date_pub = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    class Meta:
        model = Article
        fields = ("title","category", "sumary", "content", "image", "date_pub",)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)