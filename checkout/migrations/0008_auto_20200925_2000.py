# Generated by Django 3.0.7 on 2020-09-26 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0026_auto_20200810_0956'),
        ('checkout', '0007_auto_20200925_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='catalog.Movies'),
        ),
    ]