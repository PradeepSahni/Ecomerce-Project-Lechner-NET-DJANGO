# Generated by Django 3.0.9 on 2021-10-07 03:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authapp', '0002_supplier'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_name', models.CharField(max_length=191, null=True)),
                ('material_type', models.CharField(max_length=191, null=True)),
                ('material_number', models.CharField(max_length=191, null=True)),
                ('material_quantity', models.IntegerField(default=1, null=True)),
                ('price', models.IntegerField(default=0, null=True)),
                ('material_sample', models.CharField(max_length=191, null=True)),
                ('ware_house', models.CharField(max_length=191, null=True)),
                ('row_number', models.IntegerField(default=0, null=True)),
                ('material_location', models.CharField(max_length=191, null=True)),
                ('quantity_date', models.DateField(null=True)),
                ('created_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('supplier_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authapp.Supplier')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=191, null=True)),
                ('product_number', models.CharField(max_length=191, null=True)),
                ('product_step', models.CharField(max_length=191, null=True)),
                ('product_quantity', models.IntegerField(default=1, null=True)),
                ('date', models.DateField(null=True)),
                ('ware_house', models.CharField(max_length=191, null=True)),
                ('row_number', models.IntegerField(default=0, null=True)),
                ('product_location', models.CharField(max_length=191, null=True)),
                ('quantity_date', models.DateField(null=True)),
                ('product_bar_code', models.ImageField(upload_to='media/barcode/')),
                ('created_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=191, null=True)),
                ('type_of_packaging', models.CharField(max_length=191, null=True)),
                ('package_number', models.CharField(max_length=191, null=True)),
                ('internal_number', models.IntegerField(default=1)),
                ('dimension', models.CharField(max_length=191, null=True)),
                ('length', models.IntegerField(null=True)),
                ('height', models.IntegerField(null=True)),
                ('weight', models.IntegerField(null=True)),
                ('price', models.IntegerField(null=True)),
                ('date', models.DateField(null=True)),
                ('ware_house', models.CharField(max_length=191, null=True)),
                ('row_number', models.IntegerField(default=0, null=True)),
                ('package_location', models.CharField(max_length=191, null=True)),
                ('created_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('material_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lechnerapp.Material')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lechnerapp.Product')),
                ('supplier_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authapp.Supplier')),
            ],
        ),
        migrations.CreateModel(
            name='MoldingTool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('molding_name', models.CharField(max_length=191, null=True)),
                ('molding_number', models.CharField(max_length=191, null=True)),
                ('molding_status', models.IntegerField(choices=[(1, 'Active'), (0, 'Deactive')], default=1)),
                ('date', models.DateField(null=True)),
                ('ware_house', models.CharField(max_length=191, null=True)),
                ('row_number', models.IntegerField(default=0, null=True)),
                ('molding_location', models.CharField(max_length=191, null=True)),
                ('created_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('supplier_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authapp.Supplier')),
            ],
        ),
        migrations.CreateModel(
            name='MaterialImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/product/')),
                ('created_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('material_id', models.ManyToManyField(to='lechnerapp.Material')),
            ],
        ),
    ]