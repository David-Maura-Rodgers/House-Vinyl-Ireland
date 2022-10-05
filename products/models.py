from django.db import models


class Label(models.Model):
    '''
    Model for Labels which each record record is released on
    '''
    label = models.CharField(max_length=150)
    friendly_name = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        '''
        Override default str method
        '''
        return self.label

    def get_friendly_name(self):
        '''
        Returns a user friendly name for site user
        '''
        return self.friendly_name


class Record(models.Model):
    '''
    Model for the Records database
    '''
    label = models.ForeignKey(
        Label, null=True, blank=True, on_delete=models.CASCADE
    )
    title = models.CharField(max_length=254)
    artist = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    stock_quantity = models.IntegerField(default=1)
    track_list = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        '''
        Override default str method
        '''
        return self.title
