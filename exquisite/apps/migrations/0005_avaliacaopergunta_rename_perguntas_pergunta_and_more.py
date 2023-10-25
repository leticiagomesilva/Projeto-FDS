# Generated by Django 4.2 on 2023-10-25 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_perguntas'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvaliacaoPergunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avaliacao', models.CharField(choices=[('facil', 'Fácil'), ('medio', 'Médio'), ('dificil', 'Difícil')], max_length=10)),
            ],
        ),
        migrations.RenameModel(
            old_name='perguntas',
            new_name='Pergunta',
        ),
        migrations.RenameField(
            model_name='pergunta',
            old_name='pertunta',
            new_name='pergunta',
        ),
    ]
