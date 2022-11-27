from django.db import models


class Label(models.Model):
    '''
    Model for Labels which each record is released on
    '''

    class Meta:
        verbose_name_plural = 'Labels'

    label = models.CharField(max_length=150)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        '''
        Override default str method
        '''
        return self.name

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
        'Label', Label, default=False,
    )
    title = models.CharField(max_length=254)
    artist = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    stock_quantity = models.IntegerField(default=1)
    track_list_1 = models.TextField(default="Track")
    track_list_2 = models.TextField(default="Track")
    track_list_3 = models.TextField(default="Track")
    track_list_4 = models.TextField(default="Track")
    track_list_5 = models.TextField(default="Track")
    track_list_6 = models.TextField(default="Track")
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        '''
        Override default str method
        '''
        return self.title
