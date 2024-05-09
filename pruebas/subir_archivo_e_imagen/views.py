from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SubirDumentoImagenForm
from .models import SubirDumentoImagen

@login_required
def homepage(request):
    form = SubirDumentoImagenForm()
    username = request.session.get('username')  # Acceder al nombre de usuario desde la sesión
    return render(request, 'index2.html', {'form': form, 'username': username})

@login_required
def upload(request):
    if request.method == "POST":
        form = SubirDumentoImagenForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("homepage")
    else:
        form = SubirDumentoImagenForm()
    return render(request, 'index2.html', {'form': form})

@login_required
def listarData(request):
    data = SubirDumentoImagen.objects.all()
    return render(request, 'list_img_file.html', {'data': data})

@login_required
def borrar_registro(request, registro_id):
    registro = get_object_or_404(SubirDumentoImagen, id=registro_id)
    if request.method == 'POST':
        registro.delete()
        return redirect('listarData')
    return render(request, 'confirmar_borrado.html', {'registro': registro})
