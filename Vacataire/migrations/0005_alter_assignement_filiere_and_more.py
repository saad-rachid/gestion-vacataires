# Generated by Django 4.1.7 on 2023-06-27 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vacataire', '0004_rename_vacataire_assignement_vacataire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignement',
            name='filiere',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='assignement',
            name='promotion',
            field=models.IntegerField(null=True),
        ),
    ]
