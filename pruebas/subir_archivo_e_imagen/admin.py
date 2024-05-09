from django.contrib import admin
from .models import SubirDumentoImagen

class SubirDumentoImagenAdmin(admin.ModelAdmin):
    list_display = ('documento', 'created_at', 'updated')
    readonly_fields = ['created_at', 'updated']  # Hacer los campos solo de lectura para evitar ediciones accidentales
    fields = ['documento']  # Agregar el campo documento al formulario de administración

    def has_delete_permission(self, request, obj=None):
        return True  # Permitir la eliminación de documentos

    def get_deleted_objects(self, objs, request):
        deleted_objects = super().get_deleted_objects(objs, request)
        # Personalizar el mensaje de confirmación de eliminación
        if len(deleted_objects) == 1 and isinstance(deleted_objects[0], SubirDumentoImagen):
            deleted_objects[0].object_repr = str(deleted_objects[0])
        return deleted_objects

admin.site.register(SubirDumentoImagen, SubirDumentoImagenAdmin)
