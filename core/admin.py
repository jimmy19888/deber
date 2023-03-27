from django.contrib import admin

from core.models import CompraModels
from core.models import EgresoModels
from core.models import pedidoModels
from core.models import bodegaModels
from core.models import trabajadoresModels
from core.models import cant_ropasModels
from core.models import Contactos
from core.models import Princip_clientesModels
from core.models import Area_de_recursos_humanosModels
from core.models import DepartamentosModels
admin.site.register(CompraModels)
admin.site.register(EgresoModels)
admin.site.register(pedidoModels)
admin.site.register(bodegaModels)
admin.site.register(trabajadoresModels)
admin.site.register(cant_ropasModels)
admin.site.register(Contactos)
admin.site.register(Princip_clientesModels)
admin.site.register(Area_de_recursos_humanosModels)
admin.site.register(DepartamentosModels)

# Register your models here.
