from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReviewList.as_view(), name="home"),
    path("create_review/", views.CreateReview.as_view(), name="create_review"),
    path("posted_review/", views.PostedReview.as_view(), name="posted_review"),
    path("<slug:pk>/<str:title>/", views.ReviewDetail.as_view(),
         name="review_detail"),
]
