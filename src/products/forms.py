#TODO: Create ModelForms em Django Raw Forms (with validations). Remember to custom widgets attributes in each field

from django import forms


class ProductRawForm(forms.Form):
    title = forms.CharField(
        max_length=120,
        widget=forms.TextInput(attrs={
            'class': 'some-class-to-input',
            'placeholder': 'Your title here'
        })

    )
    description = forms.CharField(
        max_length=500,
        widget=forms.Textarea(attrs={
            'class': 'some-class-to-textarea second-one',
            'placeholder': 'Your description here',
            'cols': 120,
            'rows': 20
        })
    )
    # price
    # summary
    # featured
