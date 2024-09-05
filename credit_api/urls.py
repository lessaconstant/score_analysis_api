from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('banks.urls')),  
    path('api/', include('users.urls')),  
    path('api/', include('credit_analysis.urls')),  
    path('api/', include('transactions.urls')),
]
