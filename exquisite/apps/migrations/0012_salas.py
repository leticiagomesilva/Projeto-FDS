# Generated by Django 4.2 on 2023-11-20 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0011_responder'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_sala', models.TextField(max_length=255)),
                ('preferencia', models.TextField(max_length=255)),
            ],
        ),
    ]
