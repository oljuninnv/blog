# Generated by Django 4.1.3 on 2023-03-15 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_articlequestion_options_alter_image_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['date'], 'verbose_name': 'Статью', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['username'], 'verbose_name': 'Пользователя', 'verbose_name_plural': 'Пользователи'},
        ),
    ]