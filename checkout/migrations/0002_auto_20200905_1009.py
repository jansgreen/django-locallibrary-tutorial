# Generated by Django 3.0.7 on 2020-09-05 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='phone_numeber',
            new_name='phone_number',
        ),
    ]