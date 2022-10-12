from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.shortcuts import HttpResponse
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
    product = get_object_or_404(Record, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})
    quantity = 1

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    '''
    Adjust the quantity of the specified product to the specified amount
    '''

    if request.method == 'POST':
        product = get_object_or_404(Record, pk=item_id)
        quantity = request.POST.get('quantity')
        basket = request.session.get('basket', {})
        basket[item_id] = int(quantity)

        return redirect(reverse('view_basket'))
        return redirect(redirect_url)


def remove_item(request, item_id):
    '''
    Delete item from basket
    '''

    product = get_object_or_404(Record, pk=item_id)
    basket = request.session.get('basket', {})
    basket.pop(item_id)

    request.session['basket'] = basket
    return HttpResponse(status=200)
    return redirect('view_basket')
