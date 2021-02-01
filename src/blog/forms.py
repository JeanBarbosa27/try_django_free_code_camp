from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(max_length=120, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    content = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={
        'class': 'form-control'
    }))
    class Meta:
        model = Article
        fields = '__all__'
        exclude = ['slug']
