from django.db import models
from django.contrib.auth.models import User
from products.models import Record, Label

STATUS = ((0, 'Draft'), (1, 'Published'))


class Review(models.Model):
    '''
    Model for user to create reviews on records
    '''

    title = models.ForeignKey(
        Record, on_delete=models.CASCADE, max_length=100, blank=False
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=False
    )
    subject = models.CharField(
        max_length=100, null=False, blank=False, default='Enter Subject'
    )
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
        return self.subject
