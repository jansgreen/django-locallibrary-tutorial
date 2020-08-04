# Generated by Django 3.0.7 on 2020-08-04 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0022_auto_20181028_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('popularity', models.IntegerField(blank=True, default=0, null=True)),
                ('vote', models.IntegerField(blank=True, default=0, null=True)),
                ('TheatreId', models.IntegerField(blank=True, max_length=1024, null=True)),
                ('adult', models.BooleanField(blank=True, default=False, null=True)),
                ('backdrop', models.URLField(blank=True, max_length=1024, null=True)),
                ('Language', models.CharField(blank=True, max_length=5, null=True)),
                ('genreids', models.IntegerField(blank=True, default=0, null=True)),
                ('title', models.CharField(blank=True, max_length=254, null=True)),
                ('vote_average', models.IntegerField(blank=True, default=0, null=True)),
                ('overview', models.TextField(blank=True, max_length=554, null=True)),
                ('release_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Movies',
            },
        ),
    ]