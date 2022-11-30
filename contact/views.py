from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from profiles.models import UserProfile
from .forms import ContactForm


def contact(request):
    '''
    A view to return the contact page
    '''

    if request.method == "POST":
        form_data = {
            'full_name': request.POST['full_name'],
            'order_number': request.POST['order_number'],
            'email': request.POST['email'],
            'message': request.POST['message'],
        }

        contact_form = ContactForm(form_data)

        if contact_form.is_valid():
            user_contact = contact_form.save(commit=False)
            if request.user.is_authenticated:
                user = User.objects.get(username=request.user)
                user_contact.user = user
            user_contact.save()
            messages.success(
                request, "Thank you for your message, we will reply as soon \
                as we can"
            )
            return redirect(reverse('home'))
        else:
            messages.error(
                request, 'There was an error with your form. \
                Please check your information again.'
            )
            return redirect(reverse('contact'))

    else:
        contact_form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'contact_form': contact_form
    }

    return render(request, template, context)
