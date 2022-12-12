from django import forms
from .models import Newsletter


class NewsForm(forms.ModelForm):
    '''
    A form to sign up to newsletter
    '''
    class Meta:
        model = Newsletter
        fields = ('email_address',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'border-secondary'
            self.fields[field].widget.attrs['placeholder'] = 'example@example.com'  # noqa
            self.fields['email_address'].label = False
