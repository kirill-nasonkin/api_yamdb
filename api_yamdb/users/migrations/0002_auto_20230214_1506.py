# Generated by Django 3.2 on 2023-02-14 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(help_text='Введите адрес электронной почты', max_length=254, unique=True, verbose_name='Адрес эл. почты'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('user', 'user'), ('moderator', 'moderator'), ('admin', 'admin')], default='user', help_text='Выберите роль пользователя', max_length=30, verbose_name='Роль пользователя'),
        ),
    ]