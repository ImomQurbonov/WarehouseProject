from django.db import models


class Products(models.Model):
    product_name = models.CharField(max_length=50)
    product_code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.product_name


class Materials(models.Model):
    material_name = models.CharField(max_length=50)

    def __str__(self):
        return self.material_name


class ProductMaterials(models.Model):
    product = models.ForeignKey("warehouses.Products", on_delete=models.CASCADE)
    materials = models.ForeignKey("warehouses.Materials", on_delete=models.CASCADE)
    quantity = models.FloatField()


class Warehouse(models.Model):
    material = models.ForeignKey(Materials, on_delete=models.CASCADE)
    remainder = models.IntegerField()  # Ensure that this field name is spelled correctly
    price = models.DecimalField(max_digits=10, decimal_places=2)
