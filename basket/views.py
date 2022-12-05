from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.shortcuts import HttpResponse
from django.contrib import messages

from products.models import Record


def view_basket(request):
    '''
    A view that renders the bag contents page
    '''

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    '''
    Add a quantity of the specified product/record to the shopping basket
    '''
    record = get_object_or_404(Record, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(
            request, f'Updated {record.title} quantity to {basket[item_id]}'
        )
    else:
        basket[item_id] = quantity
        messages.success(request, f'ADDED: {record.title} to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    '''
    Adjust the quantity of the specified product to the specified amount
    '''

    record = get_object_or_404(Record, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
        messages.success(
            request, f'Updated {record.title} quantity to {basket[item_id]}'
        )
    else:
        basket.pop(item_id)
        messages.success(request, f'REMOVED: {record.title} from your basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_item(request, item_id):
    '''
    Delete item from basket
    '''

    try:
        record = get_object_or_404(Record, pk=item_id)
        basket = request.session.get('basket', {})

        basket.pop(item_id)
        messages.success(request, f'REMOVED: {record.title} from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)
        # return redirect('view_basket')

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
