from django.contrib import admin
from .models import Produto, Variacao


admin.site.register(Variacao)

class VariacaoInLine(admin.TabularInline):
    model = Variacao
    extra = 1


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao_curta', 'get_preco_formatado', 'get_preco_promocional_formatado')
    inlines = [VariacaoInLine]
