from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Record


def all_products(request):
    '''
    A view to display all vinyl records
    '''

    records = Record.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!"
                )
                return redirect(reverse('products'))

            queries = Q(title__icontains=query) | Q(
                description__icontains=query
            )
            records = records.filter(queries)

    context = {
        'records': records,
        'search_term': query,
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
