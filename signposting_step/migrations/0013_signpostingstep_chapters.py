# Generated by Django 3.2.3 on 2021-05-29 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signposting_step', '0012_auto_20210529_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='signpostingstep',
            name='chapters',
            field=models.CharField(blank=True, max_length=1000, verbose_name='Linked to chapters'),
        ),
    ]
