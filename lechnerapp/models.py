from django.db import models
# from django.db.models.fields import DateField
from authapp.models import Supplier
from datetime import datetime

class Product(models.Model):
    product_name = models.CharField(max_length=191,null=True)
    product_number = models.CharField(max_length=191, null=True)
    product_step = models.CharField(max_length=191, null=True)
    product_quantity = models.IntegerField(default=1,null=True)
    date = models.DateField(null=True)
    ware_house = models.CharField(max_length=191, null=True)
    row_number = models.IntegerField(default=0,null=True)
    product_location = models.CharField(max_length=191, null=True)
    quantity_date = models.DateField(null=True)
    product_bar_code = models.ImageField(upload_to ='media/barcode/')
    created_on = models.DateTimeField(default=datetime.now, blank=True)
    updated_on = models.DateTimeField(default=datetime.now, blank=True)

class Material(models.Model):
    material_name = models.CharField(max_length=191,null=True)
    material_type = models.CharField(max_length=191,null=True)
    material_number = models.CharField(max_length=191, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    material_quantity = models.IntegerField(default=1,null=True)
    price = models.IntegerField(default=0,null=True)
    material_sample = models.CharField(max_length=191, null=True)
    ware_house = models.CharField(max_length=191, null=True)
    row_number = models.IntegerField(default=0,null=True)
    material_location = models.CharField(max_length=191, null=True)
    quantity_date = models.DateField(null=True)
    created_on = models.DateTimeField(default=datetime.now, blank=True)
    updated_on = models.DateTimeField(default=datetime.now, blank=True)

class MaterialImage(models.Model):
    material = models.OneToOneField(Material, on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='media/material/')
    created_on = models.DateTimeField(default=datetime.now, blank=True)
    updated_on = models.DateTimeField(default=datetime.now, blank=True)

class MoldingTool(models.Model):
    CHOICES = [(1, 'Active'),(0, 'Deactive')]
    molding_name = models.CharField(max_length=191,null=True)
    molding_number = models.CharField(max_length=191, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    molding_status = models.IntegerField(default=1,choices=CHOICES,)
    date = models.DateField(null=True)
    ware_house = models.CharField(max_length=191, null=True)
    row_number = models.IntegerField(default=0,null=True)
    molding_location = models.CharField(max_length=191, null=True)
    created_on = models.DateTimeField(default=datetime.now, blank=True)
    updated_on = models.DateTimeField(default=datetime.now, blank=True)

class Package(models.Model):
    package_name = models.CharField(max_length=191,null=True)
    type_of_packaging = models.CharField(max_length=191, null=True)
    package_number = models.CharField(max_length=191, null=True)
    internal_number = models.IntegerField(default=1)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    dimension = models.CharField(max_length=191,null=True)
    length = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    package_quantity = models.IntegerField(default=1,null=True)
    price = models.IntegerField(null=True)
    date = models.DateField(null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ware_house = models.CharField(max_length=191, null=True)
    row_number = models.IntegerField(default=0,null=True)
    package_location = models.CharField(max_length=191, null=True)
    created_on = models.DateTimeField(default=datetime.now, blank=True)
    updated_on = models.DateTimeField(default=datetime.now, blank=True)
class ExternalPart(models.Model):
    part_name = models.CharField(max_length=191,null=True)
    part_number = models.CharField(max_length=191,null=True)
    charge_number = models.CharField(max_length=191,null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField(null=True)
    product_use_location = models.CharField(max_length=191,null=True)
    ware_house = models.CharField(max_length=191, null=True)
    row_number = models.IntegerField(default=0,null=True)
    part_location = models.CharField(max_length=191, null=True)
    created_on = models.DateTimeField(default=datetime.now, blank=True)
    updated_on = models.DateTimeField(default=datetime.now, blank=True)