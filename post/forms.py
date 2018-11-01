from django import forms
from .models import BoardTbl, CommentTbl

class PostForm(forms.ModelForm):

    class Meta:
        model = BoardTbl
        fields = ('subject' , 'content')
        labels = {
            'subject' : '제목',
            'content' : '내용',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentTbl
        fields = ('content',)
        labels = {
            'content' : '내용'
        }
        widgets = {
            'content' : forms.TextInput(),
        }