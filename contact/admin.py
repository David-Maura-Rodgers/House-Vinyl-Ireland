from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    '''
    Contact fields that will be displayed in Admin
    '''

    list_display = ('user', 'full_name', 'order_number', 'email', 'message')
    ordering = ('user',)


admin.site.register(Contact, ContactAdmin)
