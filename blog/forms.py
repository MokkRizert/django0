from django import forms

from .models import MyPost

class MyPostForm(forms.ModelForm):

    class Meta:
        model = MyPost
        fields = ('title', 'text',)