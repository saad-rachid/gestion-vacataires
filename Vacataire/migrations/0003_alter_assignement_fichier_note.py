# Generated by Django 4.1.7 on 2023-06-27 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vacataire', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignement',
            name='fichier_note',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]