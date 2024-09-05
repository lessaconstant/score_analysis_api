from django.db import models
from django.conf import settings

class CreditAnalysis(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    credit_score = models.DecimalField(max_digits=5, decimal_places=2, default=00.00)
    analysis_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - Score: {self.credit_score} - Date: {self.analysis_date}'
