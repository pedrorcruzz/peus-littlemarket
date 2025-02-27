# Generated by Django 5.1.6 on 2025-02-27 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Imagem')),
            ],
        ),
    ]
