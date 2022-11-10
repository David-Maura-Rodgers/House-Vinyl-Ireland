from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from basket.contexts import basket_contents

import stripe


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('products'))

    current_basket = basket_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LgshSHe5KRL462YAIYqkoji9NbTTaw0tVvamFWc6WnpiX6fCJ1SnGxKkEqcOwDwY8aksYJ1PqYOpJRsiiqzoSuD00fPjLY22O',  # noqa
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
