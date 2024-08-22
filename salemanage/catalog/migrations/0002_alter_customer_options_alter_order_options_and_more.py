# Generated by Django 5.1 on 2024-08-11 19:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['created_date']},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['created_date']},
        ),
        migrations.AddField(
            model_name='customer',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
