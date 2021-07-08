# Generated by Django 3.2.5 on 2021-07-08 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0010_remove_blog_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='status',
            field=models.CharField(choices=[('PUBLISHED', 'PUBLISHED'), ('PENDING', 'PENDING'), ('DECLINED', 'DECLINED')], default='PENDING', max_length=15),
        ),
    ]