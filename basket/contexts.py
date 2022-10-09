from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Record


def basket_contents(request):

    basket_items = []
    total = 0
    record_count = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        record = get_object_or_404(Record, pk=item_id)
        total += quantity * record.price
        record_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'record': record,
        })

    delivery = total * Decimal(settings.DELIVERY_PERCENTAGE / 100)
    grand_total = total + delivery

    context = {
        'basket_items': basket_items,
        'total': total,
        'record_count': record_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
