# Generated by Django 4.2 on 2023-11-24 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0015_alter_salas_preferencia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filtro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filtro_materia', models.TextField(max_length=255)),
            ],
        ),
    ]
