from django.contrib import admin
from .models import Pedido, ItemPedido


admin.site.register(ItemPedido)

class ItemPedidoInLine(admin.TabularInline):
    model = ItemPedido
    extra = 1


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    inlines = [
        ItemPedidoInLine
    ]