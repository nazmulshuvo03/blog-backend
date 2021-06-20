# Generated by Django 3.2.4 on 2021-06-20 18:48

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_user_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='created_date',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='updated_date',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, null=True),
        ),
    ]
