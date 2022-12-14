from django import forms
from .widgets import CustomClearableFileInput
from .models import Record, Label


class ProductForm(forms.ModelForm):
    '''
    Create the ProductForm class
    '''

    class Meta:
        '''
        Fields to display from Record Model
        '''

        model = Record
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        labels = Label.objects.all()
        friendly_names = [(
            label.id, label.get_friendly_name()
        ) for label in labels]

        self.fields['label'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
