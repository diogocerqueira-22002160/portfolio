# Generated by Django 4.0.4 on 2022-05-29 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cadeira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('ano', models.IntegerField(default=1)),
                ('semestre', models.IntegerField(default=1)),
                ('ano_letivo', models.IntegerField(default=1)),
                ('topicos', models.CharField(max_length=100)),
                ('ranking', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('descricao', models.CharField(max_length=500)),
                ('imagem', models.ImageField(upload_to=None)),
                ('cadeira', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Projetos', to='portfolio.cadeira')),
            ],
        ),
        migrations.AddField(
            model_name='cadeira',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Cadeiras', to='portfolio.professor'),
        ),
    ]
