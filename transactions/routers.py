# transactions/routers.py
from rest_framework import routers
from django import views
from .views import TransactionViewSet

router = routers.DefaultRouter()
router.register('transactions', views.TransactionViewSet)
