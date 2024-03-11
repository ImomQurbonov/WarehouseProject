from django.urls import path

from warehouses.views import WarehouseAPIView

urlpatterns = [
    path('warehouse/', WarehouseAPIView.as_view(), name='warehouse')
]