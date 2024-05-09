function handleDrop(event) {
    event.preventDefault();
    var files = event.dataTransfer.files;
    handleFiles(files);
}

function handleFiles(files) {
    var fileList = document.getElementById('file-list');

    for (var i = 0; i < files.length; i++) {
        var file = files[i];
        var listItem = document.createElement('li');
        listItem.textContent = file.name;
        fileList.appendChild(listItem);

        // Aquí puedes agregar el código para subir el archivo a la base de datos
    }
}

document.getElementById('drop-area').addEventListener('dragover', function(event) {
    event.preventDefault();
    this.classList.add('highlight');
});

document.getElementById('drop-area').addEventListener('dragleave', function(event) {
    event.preventDefault();
    this.classList.remove('highlight');
});

document.getElementById('drop-area').addEventListener('drop', function(event) {
    event.preventDefault();
    this.classList.remove('highlight');
    handleDrop(event);
});

document.getElementById('drop-area').addEventListener('click', function() {
    document.getElementById('file-input').click();
});

document.getElementById('file-input').addEventListener('change', function(event) {
    handleFiles(event.target.files);
});
