from django.db import models


class Label(models.Model):
    '''
    Model for Labels which each record is released on
    '''

    label = models.CharField(max_length=150)
    friendly_name = models.CharField(max_length=254)

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

    title = models.CharField(max_length=254)
    artist = models.CharField(max_length=254)
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    track = models.CharField(
        max_length=100, null=False, blank=False, default=""
    )
    description = models.TextField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        '''
        Override default str method
        '''
        return self.title

    def track_as_list(self):
        '''
        Override default str method
        '''
        return self.track.split(',')
