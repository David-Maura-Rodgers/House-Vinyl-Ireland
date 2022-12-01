from django.views.generic import View, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Review, Record, Label
from .forms import ReviewForm


class ReviewList(ListView):
    """
    This view will be rendered on the home page in a list view
    that paginates every 6 entries
    """
    model = Review
    queryset = Review.objects.filter(status=1).order_by("-created_on")
    template_name = "posted_review.html"
    paginate_by = 6


class CreateReview(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    '''
    This renders the Review page
    User can post a review on records
    '''

    model = Review
    form_class = ReviewForm
    template_name = "reviews/create_review.html"
    success_url = "/"

    def test_func(self):
        '''
        Function: test if user is authenticated
        '''

        if self.request.user.is_authenticated:
            return True
        else:
            return False

    def form_valid(self, form):
        '''
        Function: User can enter their own review using ReviewForm
        This will save the content and send to server to be authorised
        '''

        form.instance.user = self.request.user
        form.save()

        messages.success(
            self.request,
            "Your review of this record has been sent to Admin for approval"
        )

        return super(CreateReview, self).form_valid(form)


class ReviewDetail(View):
    '''
    This view will be rendered on the review detail page:
    User can see the content of posted reviews
    '''

    def get(self, request, pk, title, *args, **kwargs):
        '''
        User will be able to vote like, funny and insightful
        User can also see comments that have been made on the review
        '''

        queryset = Review.objects.filter(status=1)
        review = get_object_or_404(queryset, pk=pk)

        return render(
            request,
            "reviews/review_detail.html",
            {
                "review": review,
            },
        )
