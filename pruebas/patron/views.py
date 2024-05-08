from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
# Función para verificar si el usuario tiene el rol de gerente
def is_manager(user):
    return user.groups.filter(name='administrativo').exists()

@login_required
@user_passes_test(is_manager)  # Verificar si el usuario es un gerente
def crear_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        rol = request.POST['rol']
        
        # Validar los datos del formulario
        if (username and password and confirm_password and first_name and last_name 
            and email and rol and password == confirm_password):
            # Crear el usuario
            user = User.objects.create_user(username=username, password=password, 
                                            first_name=first_name, last_name=last_name, email=email)
            # Asignar el rol correspondiente
            if rol == 'administrativo':
                group = Group.objects.get(name='administrativo')
                user.groups.add(group)
            elif rol == 'empleado':
                group = Group.objects.get(name='empleado')
                user.groups.add(group)
            
            # Guardar el usuario en la base de datos
            user.save()


@login_required
@user_passes_test(is_manager)  # Verificar si el usuario es un gerente
def dashboard(request):
    # Obtener el nombre de usuario que ha iniciado sesión
    username = request.user.username
    # Renderizar el template y pasar el nombre de usuario
    return render(request, 'patron/dashboard.html', {'username': username})
