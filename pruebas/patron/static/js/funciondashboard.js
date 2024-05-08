document.getElementById('create-user-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const confirm_password = document.getElementById('confirm_password').value;

    if (password !== confirm_password) {
        alert("Las contraseñas no coinciden.");
        return;
    }

    // Aquí puedes enviar los datos al servidor (por ejemplo, a Django)
    console.log("Nombre de usuario:", username);
    console.log("Contraseña:", password);

    // Limpiar el formulario después de enviar los datos
    this.reset();
});

document.getElementById('user-dropdown').addEventListener('change', function() {
    const selectedUser = this.value;
    const userProfile = document.querySelector('.user-details');
    const userName = document.getElementById('user-name');
    const userEmail = document.getElementById('user-email');

    if (selectedUser) {
        userProfile.style.display = 'block';

        // Aquí puedes hacer una solicitud al servidor (por ejemplo, a Django)
        // para obtener los detalles del usuario seleccionado y luego mostrarlos en el perfil
        switch (selectedUser) {
            case 'usuario1':
                userName.textContent = 'Usuario1';
                userEmail.textContent = 'usuario1@example.com';
                break;
            case 'usuario2':
                userName.textContent = 'Usuario2';
                userEmail.textContent = 'usuario2@example.com';
                break;
            case 'usuario3':
                userName.textContent = 'Usuario3';
                userEmail.textContent = 'usuario3@example.com';
                break;
            default:
                userName.textContent = '';
                userEmail.textContent = '';
        }
    } else {
        userProfile.style.display = 'none';
    }
})
