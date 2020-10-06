# Generated by Django 3.0.7 on 2020-10-01 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0026_auto_20200810_0956'),
        ('checkout', '0011_order_town_or_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='Movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Movies'),
        ),
        migrations.AlterField(
            model_name='orderlineitem',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lineitems', to='checkout.order'),
        ),
    ]