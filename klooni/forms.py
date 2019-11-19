from django import forms
from .models import Image, Profile

class LikesNCommentsForm(forms.Form):
    likes = forms.IntegerField()
    comment = forms.CharField(label='Comment', max_length=200)
    
class UploadPicForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile','post_date', 'likes', 'comments', 'user']