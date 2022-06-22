from tienda.views import producto
from django.contrib import admin
from .models import Catalogo, Producto, Pedido, Comprador, detallePedido

# Register your models here.

admin.site.register(Catalogo)
admin.site.register(Producto)
admin.site.register(Comprador)
admin.site.register(Pedido)
admin.site.register(detallePedido)
