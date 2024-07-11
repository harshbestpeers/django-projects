from django import forms
from .models import Topic, Post

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget = forms.Textarea(
            attrs={'rows':5, 'placeholder':'what is on your mind?'}
        ),
        max_length=4000)


    class Meta:
        model = Topic
        fields = ['subject', 'message']


class ReplyPostForm(forms.ModelForm):
    message = forms.CharField(
        widget = forms.Textarea(
            attrs={'rows':5, 'placeholder':'what is on your mind?'}
        ),
        max_length=4000)

    class Meta:
        model = Post
        fields = ['message']