# Generated by Django 3.2.3 on 2021-05-29 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signposting_step', '0011_alter_signpostingstep_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='signpostingstep',
            name='sections',
            field=models.CharField(blank=True, max_length=1000, verbose_name='Linked to sections'),
        ),
        migrations.AlterField(
            model_name='signpostingstep',
            name='priority',
            field=models.IntegerField(blank=True),
        ),
    ]
