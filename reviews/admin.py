from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    '''
    Admin panel for review posts
    '''

    list_display = ('title', 'user', 'status', 'created_on')
    search_fields = ['title', 'user', 'content']
    list_filter = ('status', 'title', 'user', 'created_on')
