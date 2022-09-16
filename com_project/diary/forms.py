from django.forms import ModelForm,TextInput
from .models import Post

class UserInfoForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','content']
        widgets = {
            'title': TextInput(attrs={
                'class':"form-control",
                'style':'max-width: 300px;',
                'placeholder':'Title'
            }),
            'content': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Content'
            })
        }