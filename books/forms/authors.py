from os import name

from django import forms

from books.models import Authors


class AuthorModelForm(forms.ModelForm):
    class Meta:
        model = Authors
        fields = ('name', 'birth_date', 'biography', 'email', 'phone', 'photo')

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Author name',
                'autofocus': True,
            }),

            'birth_date': forms.SelectDateWidget(
                years=range(1900, 2027)
            ),

            'biography': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Author biography',
                'rows': 4,
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Author email',
            }),

            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Author phone',
            }),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if '@' not in email:
            raise forms.ValidationError('Email format not valid')
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) != 9:
            raise forms.ValidationError('Telefon nomer 9 ta raqam bo\'lishi kerak')
        return phone

    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        if photo and photo.size > 5*(1024 * 1024):
            raise forms.ValidationError('Photoning hajmi 5MB dan katta bo\'lmasligi kerak')
        return photo

    def clean(self):
        name = self.cleaned_data.get('name')
        biography = self.cleaned_data.get('biography')

        if biography == name:
            raise forms.ValidationError('Ikkalasi bir xil bollmasin')
