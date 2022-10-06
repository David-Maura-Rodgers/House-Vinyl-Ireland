from django.shortcuts import render
from .models import Record


def all_products(request):
    '''
    A view to display all vinyl records
    '''

    records = Record.objects.all()

    context = {
        'records': records,
    }

    return render(request, 'products/products.html', context)
