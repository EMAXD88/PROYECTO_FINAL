from django.contrib import admin
from .models import SubirDumentoImagen

class SubirDumentoImagenAdmin(admin.ModelAdmin):
    list_display = ('documento', 'created_at', 'updated')
    readonly_fields = ['created_at', 'updated']  # Hacer los campos solo de lectura para evitar ediciones accidentales
    fields = ['documento']  # Agregar el campo documento al formulario de administración

    def has_delete_permission(self, request, obj=None):
        return True  # Permitir la eliminación de documentos

admin.site.register(SubirDumentoImagen, SubirDumentoImagenAdmin)
