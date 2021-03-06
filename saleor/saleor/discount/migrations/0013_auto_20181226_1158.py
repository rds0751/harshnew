# Generated by Django 2.1.4 on 2018-12-26 06:28

from django.db import migrations, models
import django_prices.models


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0012_auto_20181226_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='type',
            field=models.CharField(choices=[('fixed', 'USD'), ('percentage', '%')], default='fixed', max_length=10),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='discount_value_type',
            field=models.CharField(choices=[('fixed', 'USD'), ('percentage', '%')], default='fixed', max_length=10),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='min_amount_spent',
            field=django_prices.models.MoneyField(blank=True, currency='USD', decimal_places=2, max_digits=12, null=True),
        ),
    ]
