from django.shortcuts import render
from .models import Record


def all_products(request):
    '''
    A view to display all vinyl records
    '''

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
