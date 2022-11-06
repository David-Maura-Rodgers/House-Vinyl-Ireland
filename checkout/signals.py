from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import ItemCheckout


@receiver(post_save, sender=ItemCheckout)
def update_on_save(sender, instance, created, **kwargs):
    '''
    Update order total for ItemCheckout when updated or created
    '''
    instance.order.calc_total()


@receiver(post_delete, sender=ItemCheckout)
def update_on_delete(sender, instance, **kwargs):
    '''
    Update order total on lineitem delete
    '''
    instance.order.calc_total()
