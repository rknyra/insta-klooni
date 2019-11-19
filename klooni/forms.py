from django import forms
from .models import *

class LikesForm(forms.Form):
    class Meta:
        model = Image
        exclude = '__all__'

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['image', 'user']
        
class UploadPicForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile','post_date','user']