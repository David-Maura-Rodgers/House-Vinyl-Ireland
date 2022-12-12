from django.contrib import admin
from .models import Newsletter


class NewsletterAdmin(admin.ModelAdmin):
    list_details = (
        'email_address',
        'agree_policy',
    )


admin.site.register(Newsletter, NewsletterAdmin)
