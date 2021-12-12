from django.urls import path

from candidates.views import CandidatesList

urlpatterns = [
    path('candidate/', CandidatesList.as_view())
]
