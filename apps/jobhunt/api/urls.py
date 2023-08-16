from django.urls import path
from .views import TotalStatsView

app_name = 'jobhunt'

urlpatterns = [
    path('totalstats/', TotalStatsView.as_view(), name='total_stats')
]