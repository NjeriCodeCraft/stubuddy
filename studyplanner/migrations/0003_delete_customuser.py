# Generated by Django 5.1.3 on 2024-12-13 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studyplanner', '0002_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]