# Generated by Django 4.2.5 on 2023-10-26 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0008_rename_meta_metas_domingo_metas_quarta_metas_quinta_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta', models.CharField(choices=[('7 perguntas', '7'), ('14 perguntas', '14'), ('21 perguntas', '21'), ('28 perguntas', '28'), ('35 perguntas', '35')], max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='Metas',
        ),
    ]
