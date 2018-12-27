# Generated by Django 2.1.4 on 2018-12-27 07:16

from django.db import migrations, models
import django_prices.models


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0013_auto_20181226_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='type',
            field=models.CharField(choices=[('fixed', 'INR'), ('percentage', '%')], default='fixed', max_length=10),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='discount_value_type',
            field=models.CharField(choices=[('fixed', 'INR'), ('percentage', '%')], default='fixed', max_length=10),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='min_amount_spent',
            field=django_prices.models.MoneyField(blank=True, currency='INR', decimal_places=2, max_digits=12, null=True),
        ),
    ]
