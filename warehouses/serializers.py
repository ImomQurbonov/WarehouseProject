from rest_framework import serializers

from warehouses.models import Warehouse, Products


class ProductSerializer(serializers.Serializer):
    product_qty = serializers.IntegerField()


class WarehouseSerializer(serializers.Serializer):
    warehouse_id = serializers.IntegerField()
    material_name = serializers.CharField()
    qty = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)

    # class Meta:
    #     model = Warehouse
    #     fields = '__all__'


class MaterialsListSerializer(serializers.Serializer):
    product_name = serializers.CharField(max_length=50)
    product_qty = serializers.FloatField()
    product_materials = serializers.ListSerializer(child=WarehouseSerializer())
