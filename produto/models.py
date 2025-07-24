from django.conf import settings
from pathlib import Path
from PIL import Image
from django.db import models
from django.utils.text import slugify
from utils import utils


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao_curta = models.TextField(max_length=255)
    descricao_longa = models.TextField()
    imagem = models.ImageField(
        upload_to='produto_imagens/%Y/%m/',
        blank=True, null=True
    )
    slug = models.SlugField(unique=True, blank=True, null=True)
    preco_marketing = models.FloatField(verbose_name='Preço')
    preco_marketing_promocional = models.FloatField(default=0, blank=True, verbose_name='Preço promocional')
    tipo = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Variação'),
            ('S', 'Simples'),
        )
    )

    def get_preco_formatado(self):
        return utils.formata_preco(self.preco_marketing)
    get_preco_formatado.short_description = 'Preço'

    def get_preco_promocional_formatado(self):
        return utils.formata_preco(self.preco_marketing_promocional)
    get_preco_promocional_formatado.short_description = 'Preço Promocional'

    @staticmethod
    def resize_image(img, new_width=800):
        img_full_path = Path(settings.MEDIA_ROOT) / img.name
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size

        if original_width <= new_width:
            img_pil.close()
            return img_pil

        new_height = round(new_width * original_height / original_width)
        new_image = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_image.save(
            img_full_path,
            optimize=True,
            quality=6,
        )

        return new_image


    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.nome)
            self.slug = slug

        super().save(*args, **kwargs)

        if self.imagem:
            max_image_size = 800
            self.resize_image(self.imagem, max_image_size)
    
    def __str__(self):
        return self.nome


class Variacao(models.Model):
    class Meta:
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, blank=True, null=True)
    preco = models.FloatField(verbose_name='Preço')
    preco_promocional = models.FloatField(default=0, blank=True, verbose_name='Preço promocional')
    estoque = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nome or self.produto.nome