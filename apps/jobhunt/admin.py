from django.contrib import admin
from apps.jobhunt.models import (
    Company,
    Vacancy,
    JobHunter
)

admin.site.register(Company)
admin.site.register(Vacancy)
admin.site.register(JobHunter)