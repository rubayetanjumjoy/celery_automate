# Generated by Django 4.2.9 on 2024-02-09 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automate', '0003_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('electronics', 'Electronics'), ('clothing', 'Clothing'), ('books', 'Books'), ('home_appliances', 'Home Appliances')], max_length=50),
        ),
    ]
