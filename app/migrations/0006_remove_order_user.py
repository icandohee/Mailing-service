# Generated by Django 5.0.6 on 2024-05-17 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
    ]
