from django.urls import path
from .views import CreditAnalysisView

urlpatterns = [
    path('analyze-credit/', CreditAnalysisView.as_view(), name='analyze_credit'),
]
