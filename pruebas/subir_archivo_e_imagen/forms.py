from django import forms
from .models import SubirDumentoImagen

class SubirDumentoImagenForm(forms.ModelForm):
    class Meta:
        model = SubirDumentoImagen
        fields = ('documento',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['documento'].widget.attrs.update(
            {'accept': '.pdf, .doc, .docx, .txt, .xlsx'})  # Permitir documentos y Excel
