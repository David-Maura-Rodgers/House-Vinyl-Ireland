from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import NewsForm


def newsletter(request):
    '''
    View for user to register for newsletter
    '''
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Email address successfully\
                 registered. Thank you.')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Please enter a valid email address')
    else:
        form = NewsForm()

    template = 'newsletter/news.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
