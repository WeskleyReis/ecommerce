from django.contrib import admin
from .models import Produto, Variacao


admin.site.register(Variacao)

class VariacaoInLine(admin.TabularInline):
    model = Variacao
    extra = 1


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    inlines = [VariacaoInLine]