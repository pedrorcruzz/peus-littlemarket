# Generated by Django 5.1.6 on 2025-02-27 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Produto', 'verbose_name_plural': 'Produtos'},
        ),
    ]
