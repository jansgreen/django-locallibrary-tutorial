# Generated by Django 3.0.7 on 2020-10-05 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0021_auto_20201005_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
