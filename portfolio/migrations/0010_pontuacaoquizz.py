# Generated by Django 4.0.4 on 2022-05-29 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_alter_cadeira_imagem_alter_professor_imagem_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PontuacaoQuizz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('pontuacao', models.IntegerField(default=0)),
            ],
        ),
    ]
