# Generated by Django 5.2 on 2025-07-12 11:43

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_alter_document_content_alter_document_content_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='content',
            field=ckeditor.fields.RichTextField(default=1, verbose_name='Содержание документа'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='document',
            name='content_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Содержание документа'),
        ),
        migrations.AlterField(
            model_name='document',
            name='content_ky',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Содержание документа'),
        ),
        migrations.AlterField(
            model_name='document',
            name='content_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Содержание документа'),
        ),
        migrations.AlterField(
            model_name='document',
            name='title',
            field=models.CharField(default=1, max_length=255, verbose_name='Заголовок документа'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='document',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок документа'),
        ),
        migrations.AlterField(
            model_name='document',
            name='title_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок документа'),
        ),
        migrations.AlterField(
            model_name='document',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок документа'),
        ),
    ]
