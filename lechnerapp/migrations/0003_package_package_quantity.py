# Generated by Django 3.0.9 on 2021-10-14 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lechnerapp', '0002_auto_20211014_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='package_quantity',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
