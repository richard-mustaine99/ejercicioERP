from django.contrib import admin
from .models import Empresa
from .models import Contacto
from .models import Relaciones

admin.site.register(Empresa)
admin.site.register(Contacto)
admin.site.register(Relaciones)