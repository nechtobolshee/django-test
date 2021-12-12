from rest_framework import serializers
from .models import Candidate, WorkExperience
# import json


class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = ['start', 'end']


class CandidateSerializer(serializers.ModelSerializer):
    work_experience = WorkExperienceSerializer(many=True, read_only=True)

    class Meta:
        model = Candidate
        fields = ['id', 'name', 'total_experience', 'work_experience']
        # queryset = Candidate.objects.order_by('-total_experience')
        # responseJSON3 = json.loads(Candidate.objects)
        # ordering = sorted(responseJSON3['Candidate'], key=lambda x:x['total_experience'])

