# Generated by Django 4.2 on 2023-11-23 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0012_salas'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pergunta',
        ),
        migrations.AlterField(
            model_name='salas',
            name='preferencia',
            field=models.TextField(choices=[('FDS', 'Fundamento De Desenvolvimento De Software'), ('Math', 'Matematica'), ('Hist', 'Historia'), ('Portu', 'Portugues'), ('Geo', 'Geografia'), ('Cien', 'Ciencias')], max_length=10),
        ),
    ]
