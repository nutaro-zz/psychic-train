from django.contrib import admin
from .models import Client, Telefone, Email

admin.site.register(Client)
admin.site.register(Telefone)
admin.site.register(Email)

