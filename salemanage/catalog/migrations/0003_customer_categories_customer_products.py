# Generated by Django 5.1 on 2024-08-12 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_customer_options_alter_order_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='categories',
            field=models.ManyToManyField(help_text='select category for this customer', to='catalog.catagory'),
        ),
        migrations.AddField(
            model_name='customer',
            name='products',
            field=models.ManyToManyField(help_text='select product for this customer', to='catalog.product'),
        ),
    ]
