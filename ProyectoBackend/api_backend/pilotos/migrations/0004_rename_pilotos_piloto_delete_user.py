# Generated by Django 5.0.3 on 2024-06-18 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pilotos', '0003_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pilotos',
            new_name='Piloto',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
