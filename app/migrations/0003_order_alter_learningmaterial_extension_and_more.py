# Generated by Django 5.0.6 on 2024-05-16 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_learningmaterial_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('total_price', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='learningmaterial',
            name='extension',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='learningmaterial',
            name='file_path',
            field=models.CharField(max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='learningmaterial',
            name='file_size',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='learningmaterial',
            name='original_filename',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='learningmaterial',
            name='stored_filename',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
