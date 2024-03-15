# Generated by Django 4.1.7 on 2023-06-26 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Absence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('justifiee', models.BooleanField(default=False)),
                ('motif', models.CharField(default='malade', max_length=50)),
                ('justif', models.FileField(null=True, upload_to=None)),
            ],
        ),
        migrations.CreateModel(
            name='Assignement',
            fields=[
                ('filiere', models.CharField(max_length=10)),
                ('promotion', models.IntegerField()),
                ('element', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('fichier_note', models.FileField(null=True, upload_to=None)),
            ],
        ),
        migrations.CreateModel(
            name='Presence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horraire', models.DateTimeField(auto_now_add=True)),
                ('present', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Seance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jour', models.CharField(max_length=15)),
                ('horaire', models.TimeField()),
                ('date_seance', models.DateField()),
                ('type', models.CharField(choices=[('TP', 'TP'), ('COURS', 'COURS'), ('TD', 'TD'), ('CC', 'CC')], max_length=50)),
                ('salle', models.CharField(max_length=10)),
            ],
        ),
    ]
