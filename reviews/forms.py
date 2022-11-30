from .models import Comment
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
        fields = ('title', 'user', 'artist', 'label', 'content',)
