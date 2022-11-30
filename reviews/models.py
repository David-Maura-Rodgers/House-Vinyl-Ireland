from django.db import models
from django.contrib.auth.models import User
from products.models import Record, Label

STATUS = ((0, 'Draft'), (1, 'Published'))


class Review(models.Model):
    '''
    Model for user to create reviews on records
    '''

    title = models.CharField(Record, max_length=100, blank=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=False
    )
    artist = models.CharField(Record, max_length=100, blank=False)
    label = models.CharField(Label, max_length=100, blank=True, default='')
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        '''
        Order review posts by dates they are created on
        '''
        ordering = ["-created_on"]

    def __str__(self):
        '''
        Override default str method
        '''
        return self.title
