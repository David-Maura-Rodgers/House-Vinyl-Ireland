from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    '''
    Create a form with fields for user to enter data in
    '''

    class Meta:
        '''
        Fields needed to render form model
        '''

        model = Contact
        fields = ('full_name', 'order_number', 'email', 'message',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['full_name'].widget.attrs['placeholder'] = 'Enter Name'  # noqa
            self.fields['order_number'].widget.attrs['placeholder'] = '(optional)'  # noqa
            self.fields['email'].widget.attrs['placeholder'] = 'example@example.com'  # noqa
            self.fields['message'].widget.attrs['placeholder'] = 'Message'
