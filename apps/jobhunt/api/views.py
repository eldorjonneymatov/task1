from rest_framework.views import APIView
from rest_framework.response import Response
from apps.jobhunt.models import (
    Company,
    Vacancy,
    JobHunter
)


class TotalStatsView(APIView):
    def get(self, request, format=None):
        data = {}
        data['company_count'] = Company.objects.count()
        data['vacancy_count'] = Vacancy.objects.count()
        data['jobhunter_count'] = JobHunter.objects.count()
        return Response(data)