from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import CustomUser
from .models import CreditAnalysis
from .ml_models import predict_credit_score

class CreditAnalysisView(APIView):
    
    def get(self, request, user_id):
        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return Response({'error': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            credit_analysis = CreditAnalysis.objects.get(user=user)
            return Response({'credit_score': credit_analysis.credit_score}, status=status.HTTP_200_OK)
        except CreditAnalysis.DoesNotExist:
            return Response({'error': 'Análise de crédito não encontrada'}, status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        user_id = request.data.get('user_id')
        if not user_id:
            return Response({'error': 'user_id é necessário'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return Response({'error': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        # Dados do usuário
        user_data = {
            'age': user.age,
            'gender': 1 if user.gender == 'M' else 0, 
            'dependents': user.dependents,
            'education_level': user.education_level,
            'annual_income': user.annual_income,
            'card_type': user.card_type,
            'products_purchased_12m': user.products_purchased_12m,
            'interactions_12m': user.interactions_12m,
            'inactive_months_12m': user.inactive_months_12m,
            'credit_limit': user.credit_limit,
            'transaction_value_12m': user.transaction_value_12m,
            'transaction_count_12m': user.transaction_count_12m
        }

        # Previsão do score de crédito
        credit_score = predict_credit_score(user_data)

        # Criação da análise de crédito
        CreditAnalysis.objects.create(
            user=user,
            credit_score=credit_score
        )
        
        return Response({'credit_score': credit_score}, status=status.HTTP_200_OK)
