# Generated by Django 4.2.9 on 2024-11-14 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quest', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='name',
        ),
    ]
