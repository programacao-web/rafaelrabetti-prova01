# Generated by Django 2.0.5 on 2018-05-10 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('linguagem', models.CharField(choices=[('Python', 'Python'), ('Javascript', 'Javascript'), ('Outros', 'Outros')], max_length=200)),
                ('conteudo', models.TextField()),
            ],
        ),
    ]