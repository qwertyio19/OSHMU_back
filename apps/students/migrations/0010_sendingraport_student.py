# Generated by Django 5.2 on 2025-07-15 07:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_alter_sendingraport_dedline_tasks_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sendingraport',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sending_raports', to='students.studentprofile'),
        ),
    ]
