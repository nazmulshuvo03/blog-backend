# Generated by Django 3.2.4 on 2021-06-20 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20210620_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='meta_title',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
    ]
