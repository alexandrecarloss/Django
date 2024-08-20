from django.contrib import admin

from .models import *
admin.site.register(Produto)
admin.site.register(Vendedor)
admin.site.register(Vendas)