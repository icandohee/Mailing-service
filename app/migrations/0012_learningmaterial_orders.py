# Generated by Django 5.0.6 on 2024-05-18 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_rename_to_email_order_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='learningmaterial',
            name='orders',
            field=models.ManyToManyField(to='app.order'),
        ),
    ]
