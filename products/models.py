from django.db import models


class Label(models.Model):
    '''
    Model for Labels which each record record is released on
    '''
    label = models.CharField(max_length=150)
    friendly_name = models.CharField(max_length=150, null=True, blank=True)
