# Generated by Django 5.1 on 2024-09-04 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0007_fotografia_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='publicada',
            field=models.BooleanField(default=True),
        ),
    ]
