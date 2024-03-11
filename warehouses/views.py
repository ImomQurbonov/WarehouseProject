from rest_framework.response import Response
from rest_framework.views import APIView
from warehouses.models import Products, Materials, ProductMaterials, Warehouse
from warehouses.serializers import  MaterialsListSerializer


class WarehouseAPIView(APIView):
    def get(self, request):
        product_ids = [
            {'product_id': 1, 'quantity': 30},
            {'product_id': 2, 'quantity': 20}
        ]

        result = []

        for item in product_ids:
            product_id = item["product_id"]
            quantity = item["quantity"]
            product = Products.objects.get(pk=product_id)
            materials = ProductMaterials.objects.filter(product=product_id)
            product_materials = []

            for material in materials:
                warehouses = Warehouse.objects.filter(material=material.materials_id).order_by('price')

                remaining_quantity = quantity * material.quantity
                material_name = Materials.objects.get(pk=material.materials_id)

                for warehouse in warehouses:
                    if remaining_quantity <= 0:
                        break

                    available_quantity = min(remaining_quantity, warehouse.remainder)
                    remaining_quantity -= available_quantity

                    product_materials.append({
                        'warehouse_id': warehouse.id,
                        'material_name': material_name,
                        'qty': available_quantity,
                        'price': warehouse.price
                    })

            if remaining_quantity > 0:
                product_materials.append({
                    'warehouse_id': None,
                    'material_name': material_name,
                    'qty': remaining_quantity,
                    'price': None
                })

            result.append({
                'product_name': product,
                'product_qty': quantity,
                'product_materials': product_materials
            })

        serializer = MaterialsListSerializer(result, many=True)
        return Response(serializer.data)

