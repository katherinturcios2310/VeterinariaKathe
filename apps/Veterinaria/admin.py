from django.contrib import admin

from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.


#Modelo2
class resourcecolores (resources.ModelResource):
    class Meta:
        model = colores

class admincolores(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['color']
    list_display = ['color']
    resource_class = resourcecolores

admin.site.register(colores, admincolores)

#Modelo3
class resourceespecies (resources.ModelResource):
    class Meta:
        model = especies

class adminespecies(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['especie']
    list_display = ['especie']
    resource_class = resourceespecies

admin.site.register(especies, adminespecies)

#Modelo4
class resourcerazas (resources.ModelResource):
    class Meta:
        model = razas

class adminrazas(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['raza']
    list_display = ['raza']
    resource_class = resourcerazas

admin.site.register(razas, adminrazas)

#Modelo1
class resourceanimales (resources.ModelResource):
    class Meta:
        model = animales

class adminanimales(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['nombre', 'diagnostico', 'medicamentos', 'descripcion']
    resource_class = resourceanimales

admin.site.register(animales, adminanimales)
