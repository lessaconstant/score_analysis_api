from rest_framework import serializers
from .models import CreditAnalysis
from users.serializers import CustomUserSerializer

class CreditAnalysisSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True) 

    class Meta:
        model = CreditAnalysis
        fields = ['id', 'user', 'credit_score', 'analysis_date']
