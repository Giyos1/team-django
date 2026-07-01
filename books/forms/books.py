from django import forms

from books.models import Books


class BookForm(forms.Form):
    name = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'text kirit',
        'autofocus': True
    }))
    price = forms.IntegerField()

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError('3 ta harfdan kop bolsin')

        return name

    def clean(self):
        name = self.cleaned_data.get('name')
        description = self.cleaned_data.get('description')

        if description == name:
            raise forms.ValidationError('ikkalasi bir xil bollmasin')

        return self.cleaned_data

    # def save(self):
    #     pass


class BookModelForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ('name', 'description', 'price', 'author')
        widgets = {
            "name": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Book name',
                'autofocus': True
            }),
            "description": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Book description',
                'autofocus': True
            }),
            "price": forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Book price',
            }),
            "author": forms.Select(attrs={
                'class': 'form-control',
            }),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError('3 ta harfdan kop bolsin')

        return name

    def clean(self):
        name = self.cleaned_data.get('name')
        description = self.cleaned_data.get('description')

        if description == name:
            raise forms.ValidationError('ikkalasi bir xil bollmasin')

        return self.cleaned_data
