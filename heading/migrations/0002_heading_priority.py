# Generated by Django 3.2.3 on 2021-05-28 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heading', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='heading',
            name='priority',
            field=models.CharField(blank=True, max_length=2),
        ),
    ]
