from django.urls import path
from .views import ChallengeView,ChallengeDetail

urlpatterns = [
    path('challenge/',ChallengeView.as_view(), name='challenge_data'),
    path('challenge/<int:pk>/',ChallengeDetail.as_view(), name='challenge_result')
]