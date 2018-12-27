# Generated by Django 2.1.4 on 2018-12-26 06:28

from django.db import migrations
import django_prices.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0082_auto_20181226_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=django_prices.models.MoneyField(currency='USD', decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='cost_price',
            field=django_prices.models.MoneyField(blank=True, currency='USD', decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='price_override',
            field=django_prices.models.MoneyField(blank=True, currency='USD', decimal_places=2, max_digits=12, null=True),
        ),
    ]
