# Generated by Django 3.0.7 on 2020-10-01 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0009_auto_20200925_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='town_or_city',
        ),
    ]
