# Generated by Django 4.2.2 on 2024-02-07 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_plan_hour_plan_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='time',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
