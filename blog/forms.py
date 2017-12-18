from django  import forms
from .models import Post,Like,Comment



class PostUploadForm(forms.ModelForm):

    class Meta:
        model=Post
        fields=('title','text','image')




class CommentForm(forms.ModelForm):

    class Meta:
        model=Comment
        fields=('body',)

