# Generated by Django 2.1.4 on 2018-12-22 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0067_auto_20181102_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping_company',
            field=models.CharField(blank=True, editable=False, max_length=36),
        ),
    ]
