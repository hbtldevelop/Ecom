# Generated by Django 5.0.1 on 2024-01-16 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_products_cfm'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='earning',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True),
        ),
    ]
