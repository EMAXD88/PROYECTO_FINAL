from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import ensure_csrf_cookie
from .forms import LoginForm

@ensure_csrf_cookie
def custom_login(request):
    error_message = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['username'] = username  # Guardamos el nombre de usuario en la sesión
                if user.groups.filter(name='administrativo').exists():
                    return redirect('admin:index')  # Redirigir al panel de administración
                elif user.groups.filter(name='empleado').exists():
                    return redirect('homepage')  # Redirigir a la vista de empleados
            else:
                error_message = "Nombre de usuario o contraseña incorrectos."
        else:
            error_message = "Por favor, corrija los errores en el formulario."
    else:
        form = LoginForm()
    return render(request, 'login/index.html', {'form': form, 'error_message': error_message})
