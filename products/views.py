from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.db.models import Q

from .models import Record, Label
from .forms import ProductForm


def all_products(request):
    '''
    A view to display all vinyl records
    '''

    records = Record.objects.all()
    query = None
    labels = None

    if 'label' in request.GET:
        labels = request.GET['label'].split(',')
        records = products.filter(label__name__in=labels)
        labels = Label.objects.filter(name__in=labels)

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
        'current_labels': labels,
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


def add_product(request):
    '''
    Allow superuser/admin to add a product to the store
    '''

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added new record!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the \
                form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_product(request, record_id):
    '''
    Edit a record in the store
    '''

    record = get_object_or_404(Record, pk=record_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated record!')
            return redirect(reverse('product_detail', args=[record.id]))
        else:
            messages.error(request, 'Failed to update record. Please ensure \
                the form is valid.')
    else:
        form = ProductForm(instance=record)
        messages.info(request, f'You are editing {record.title}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'record': record,
    }

    return render(request, template, context)
