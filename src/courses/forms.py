from django import forms

from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

    def clean_title(self):
        title = self.cleaned_data.get('title')

        if title.lower() == 'abc':
            raise forms.ValidationError('This title is not valid!')

        return title
