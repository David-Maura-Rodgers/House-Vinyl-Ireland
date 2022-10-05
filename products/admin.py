from django.contrib import admin
from .models import Label, Record, Image


class LabelAdmin(admin.ModelAdmin):
    '''
    Change Label of Record
    '''
    list_display = ('friendly_name',)
    ordering = ('friendly_name',)


class RecordAdmin(admin.ModelAdmin):
    '''
    Change details of each Record
    '''
    list_display = (
        'artist',
        'label',
        'title',
        'stock_quantity',
    )
    ordering = ('artist',)


class ImageAdmin(admin.ModelAdmin):
    '''
    Change image for each Record
    '''
    list_display = ('image_name', 'image', 'record')
    ordering = ('record',)


admin.site.register(Label, LabelAdmin)
admin.site.register(Record, RecordAdmin)
admin.site.register(Image, ImageAdmin)
