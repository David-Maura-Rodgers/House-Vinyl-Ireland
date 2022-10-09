from decimal import Decimal
from django.conf import settings


def bag_contents(request):

    basket_items = []
    total = 0
    record_count = 0

    context = {
        'basket_items': basket_items,
        'total': total,
        'record_count': record_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
