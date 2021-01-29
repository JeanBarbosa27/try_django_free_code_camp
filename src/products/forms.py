from django import forms
from .models import Product


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
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'some-class-to-textarea second-one',
            'placeholder': 'Your description here',
            'cols': 120,
            'rows': 20
        })
    )
    price = forms.DecimalField(initial=9.99)
    summary = forms.CharField(
        max_length=500,
        widget=forms.Textarea(attrs={
            'class': 'some-class-to-input',
            'placeholder': 'Your summary here',
            'cols': 120,
            'rows': 20
        })
    )
    featured = forms.BooleanField(required=False, initial=False)

    def clean_title(self):
        title = self.cleaned_data['title']

        if not 'try django product' in title:
            raise forms.ValidationError('This title is not valid, it must contais "try django product" in it!')

        return title


class ProductModelForm(forms.ModelForm):
    initial_description_value = 'In this case you can see the difference when the defaults configurations comes in summary field, in comparison with description field.'

    title = forms.CharField(max_length=120, widget=forms.TextInput(attrs={
        'class': 'some-class-to-input-field second-one',
        'placeholder': 'Your product title here'
    }))
    description = forms.CharField(
        max_length=500,
        required=False,
        initial=initial_description_value,
        widget=forms.Textarea(attrs={
            'class': 'some-class-to-textarea-field and-second-one',
            'placeholder': 'Your description here',
            'cols': 120,
            'rows': 20,
            'id': 'some-specific-id-to-this-textarea'
        }))
    price = forms.DecimalField(initial=19.99)
    class Meta:
        model = Product
        fields = '__all__'

    def clean_price(self):
        price = self.cleaned_data['price']

        if price == 0.00:
            raise forms.ValidationError('The price must be greater than 0.00')

        return price
