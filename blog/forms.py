from django import forms
from blog.models import Post
from django.utils import timezone


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('header', 'content', 'image', 'tags', 'blog', 'author')


class DateTimeForm(forms.Form):
    thisyear = timezone.now().year
    year = forms.IntegerField(max_value=thisyear)
    month = forms.IntegerField(max_value=12)
    day = forms.IntegerField(max_value=31)

    class Meta:
        fields = ('year', 'month', 'day')
