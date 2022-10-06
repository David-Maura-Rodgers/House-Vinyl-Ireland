from django.shortcuts import render, get_object_or_404
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


def product_detail(request, record_id):
    '''
    A view to display further details on each record
    '''

    record = get_object_or_404(Record, pk=record_id)

    context = {
        'record': record,
    }

    return render(request, 'products/product_detail.html', context)
