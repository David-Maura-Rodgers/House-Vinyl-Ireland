from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    '''
    Allows site user to contact site owner
    '''

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )
    full_name = models.CharField(max_length=254, null=False, blank=False)
    order_number = models.CharField(max_length=32, null=True, blank=True)
    email = models.EmailField(max_length=254, null=False, blank=False)
    message = models.TextField(null=True, blank=True)
    message_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        '''
        Order messages by date
        '''
        ordering = ['-message_date']

    def __str__(self):
        return self.full_name
