# Generated by Django 5.2 on 2025-07-13 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='full_name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Полное имя'),
        ),
    ]
