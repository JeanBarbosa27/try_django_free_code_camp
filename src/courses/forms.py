from django import forms

from .models import Course


class CourseForm(forms.ModelForm):
    title = forms.CharField(max_length=120, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    description = forms.CharField(max_length=500, widget=forms.Textarea(attrs={
        'class': 'form-control'
    }))
    class Meta:
        model = Course
        fields = '__all__'

    def clean_title(self):
        title = self.cleaned_data.get('title')

        if title.lower() == 'abc':
            raise forms.ValidationError('This title is not valid!')

        return title
