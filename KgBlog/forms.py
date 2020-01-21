from django import forms
from .models import Post
import datetime
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['post_title', 'post_text']
        exclude = ['pub_date']

