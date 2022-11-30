from django.views.generic import View, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Review, Record, Label
from .forms import ReviewForm


class CreateReview(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    '''
    This renders the Review page
    User can post a review on records
    '''
    model = Review
    form_class = ReviewForm
    template_name = "record_reviews.html"
    success_url = "/"

    def test_func(self):
        """
        Function: test if user(gamer) is authenticated
        """
        if self.request.user.is_authenticated:
            return True
        else:
            return False

    def form_valid(self, form):
        """
        Function: User can enter their own review using ReviewForm
        This will save the content and send to server to be authorised
        """
        form.instance.user = self.request.user
        form.save()

        messages.success(
            self.request,
            "Your review of this record has been sent to Admin for approval"
        )

        return super(CreateReview, self).form_valid(form)
