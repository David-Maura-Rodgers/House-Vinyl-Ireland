from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    '''
    Admin panel for review posts
    '''

    list_display = ('title', 'user', 'subject', 'status', 'created_on')
    search_fields = ['title', 'user', 'subject', 'content']
    list_filter = ('status', 'title', 'user', 'created_on')
    actions = ["approve_reviews"]

    def approve_review(self, request, queryset):
        '''
        For Admin to approve reviews
        '''
        queryset.update(approved=True)
