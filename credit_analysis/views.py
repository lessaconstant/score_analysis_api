from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import CustomUser
from .models import CreditAnalysis
from .ml_models import predict_credit_score

class CreditAnalysisView(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        if not user_id:
            return Response({'error': 'user_id é necessário'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return Response({'error': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
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
            'transaction_count_12m': user.transaction_count_12m,
        }

        # Fazer a previsão usando o modelo carregado
        credit_score = predict_credit_score(user_data)

        # Criar a entrada de análise de crédito
        CreditAnalysis.objects.create(
            user=user,
            credit_score=credit_score
        )
        
        return Response({'credit_score': credit_score}, status=status.HTTP_200_OK)
