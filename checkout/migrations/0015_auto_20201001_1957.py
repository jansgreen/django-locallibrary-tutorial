# Generated by Django 3.0.7 on 2020-10-01 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0014_auto_20201001_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='lineitem_total',
            field=models.IntegerField(),
        ),
    ]
