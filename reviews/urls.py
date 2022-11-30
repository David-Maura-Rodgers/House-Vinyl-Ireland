from django.urls import path
from . import views

urlpatterns = [
    path("create_review/", views.CreateReview.as_view(), name="create_review"),
    path("<slug:pk>/<str:title>/", views.ReviewDetail.as_view(),
         name="review_detail"),
]
