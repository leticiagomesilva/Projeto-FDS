# Generated by Django 4.2 on 2023-11-23 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0013_delete_pergunta_alter_salas_preferencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salas',
            name='preferencia',
            field=models.TextField(max_length=10),
        ),
    ]
