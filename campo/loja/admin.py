from django.contrib import admin
from .models import Produto, Fornecedore

# Register your models here.

admin.site.register(Produto)
admin.site.register(Fornecedore)