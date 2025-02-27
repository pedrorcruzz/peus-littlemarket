from django.db import models

class Product(models.Model):
    name: models.CharField = models.CharField(max_length=255, verbose_name="Nome")
    description: models.TextField = models.TextField(null=True, blank=True, verbose_name="Descrição")
    price: models.DecimalField = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")
    image: models.ImageField = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name="Imagem")

    class Meta:
        db_table = "products" 
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self) -> str:
        return self.name
