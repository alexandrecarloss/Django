from django.urls import path
from .views import ProdutoAPIView, prod

urlpatterns = [
    path('produtos/', ProdutoAPIView.as_view(), name='produtos'),
    path('prod/', prod, name='prod'),
]