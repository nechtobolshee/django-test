from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from candidates.models import Candidate, WorkExperience
from candidates.serializers import CandidateSerializer


def str_to_date(date):
    return datetime.strptime(date, '%b %Y')


class CandidatesList(APIView):
    def get(self, request, format=None):
        candidates = Candidate.objects.all()
        serializer = CandidateSerializer(candidates, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data

        candidate = Candidate.objects.filter(name=data.get('name')).first()
        if not candidate:
            candidate = Candidate.objects.create(name=data.get('name'))

        for work_exp in data.get('workExperience'):
            WorkExperience.objects.create(
                candidate=candidate,
                start=str_to_date(work_exp.get('start')),
                end=str_to_date(work_exp.get('end'))
            )

        return Response(status.HTTP_201_CREATED)

