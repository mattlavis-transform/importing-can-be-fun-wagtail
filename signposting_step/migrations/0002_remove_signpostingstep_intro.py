# Generated by Django 3.2.3 on 2021-05-28 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signposting_step', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signpostingstep',
            name='intro',
        ),
    ]
