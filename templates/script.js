document.getElementById('imageForm').addEventListener('submit', function(event) {
    // Empêche la soumission du formulaire (rechargement de la page)
    event.preventDefault();

    // Récupère les entrées du formulaire
    const imageInput = document.getElementById('image');
    const descriptionInput = document.getElementById('description');

    const file = imageInput.files[0]; // L'image choisie
    const description = descriptionInput.value; // La description

    // Vérifie si une image a été sélectionnée
    if (!file) {
        alert('Veuillez sélectionner une image.');
        return;
    }

    // Crée un objet URL pour l'image (lien temporaire)
    const imageUrl = URL.createObjectURL(file);

    // Crée la carte d'image et la description à ajouter à la galerie
    const imageCard = document.createElement('div');
    imageCard.classList.add('image-card');
    imageCard.innerHTML = `
        <img src="${imageUrl}" alt="Image" style="width: 200px; height: 200px;">
        <p>Description: ${description}</p>
    `;

    // Ajoute la carte à la galerie
    document.querySelector('.gallery').appendChild(imageCard);

    // Réinitialise le formulaire pour permettre un nouvel ajout
    imageInput.value = ''; // Réinitialise le champ de fichier
    descriptionInput.value = ''; // Réinitialise la description
});


let imagesData = [];

// Fonction pour charger et lire le fichier CSV
function loadCSV(file) {
    const reader = new FileReader();
    reader.onload = function(event) {
        const csvContent = event.target.result;
        const lines = csvContent.split('\n');
        const headers = lines[0].split(',');

        imagesData = lines.slice(1).map(line => {
            const values = line.split(',');
            return { image: values[0], description: values[1] };
        });

        // Afficher la galerie
        displayGallery();
    };
    reader.readAsText(file);
}

// Affichage des images dans la galerie
function displayGallery() {
    const gallery = document.getElementById('gallery');
    gallery.innerHTML = '';

    imagesData.forEach(data => {
        const imageCard = document.createElement('div');
        imageCard.classList.add('image-card');

        const image = document.createElement('img');
        image.src = `images/${data.image}`;
        image.alt = data.description;

        const description = document.createElement('p');
        description.textContent = data.description;

        imageCard.appendChild(image);
        imageCard.appendChild(description);
        gallery.appendChild(imageCard);
    });
}

// Fonction pour ajouter une image à la galerie
document.getElementById('image-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const imageInput = document.getElementById('image').value;
    const descriptionInput = document.getElementById('description').value;

    imagesData.push({ image: imageInput, description: descriptionInput });

    document.getElementById('image-form').reset();
    displayGallery();
});

// Charger le fichier CSV lorsque la page est prête
document.addEventListener('DOMContentLoaded', function() {
    const csvFileInput = document.createElement('input');
    csvFileInput.type = 'file';
    csvFileInput.accept = '.csv';
    csvFileInput.addEventListener('change', function(event) {
        const file = event.target.files[0];
        if (file) {
            loadCSV(file);
        }
    });

    document.body.appendChild(csvFileInput);
});
