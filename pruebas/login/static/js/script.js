document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("misionLink").addEventListener("click", function(event) {
      event.preventDefault();
      document.getElementById("mision").style.display = 'block';
      document.getElementById("vision").style.display = 'none';
      document.getElementById("ubicacion").style.display = 'none';
    });
  
    document.getElementById("visionLink").addEventListener("click", function(event) {
      event.preventDefault();
      document.getElementById("mision").style.display = 'none';
      document.getElementById("vision").style.display = 'block';
      document.getElementById("ubicacion").style.display = 'none';
    });
  
    document.getElementById("ubicacionLink").addEventListener("click", function(event) {
      event.preventDefault();
      document.getElementById("mision").style.display = 'none';
      document.getElementById("vision").style.display = 'none';
      document.getElementById("ubicacion").style.display = 'block';
    });
  });
  