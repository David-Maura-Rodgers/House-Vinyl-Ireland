from .models import Review
from django import forms


class ReviewForm(forms.ModelForm):
    '''
    Users can post a review
    '''
    class Meta:
        '''
        Model and fields needed for reviews
        '''
        model = Review
        fields = ('title', 'content',)
