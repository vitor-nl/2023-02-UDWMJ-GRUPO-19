# Generated by Django 4.2.7 on 2023-12-01 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmes',
            name='resumo_filme',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]