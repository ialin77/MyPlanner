# Generated by Django 4.2.2 on 2024-02-08 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_plan_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Plan',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]