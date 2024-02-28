# Generated by Django 4.2.9 on 2024-02-08 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('electronics', 'Electronics'), ('clothing', 'Clothing'), ('books', 'Books')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]