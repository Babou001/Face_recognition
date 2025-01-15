  Projet de Reconnaissance Faciale

Ce projet implémente un système de reconnaissance faciale en utilisant un ensemble de données composé de 30 photos de différentes personnes. Le système utilise des techniques de machine learning et de vision par ordinateur pour identifier et reconnaître les visages. Vous trouverez ci-dessous les détails sur le projet, sa structure et les instructions pour l'installation et l'utilisation.

1. Fonctionnalités

- Détection Faciale : Identifie les visages dans les images d'entrée.

- Reconnaissance Faciale : Associe les visages détectés à un ensemble de données de 30 images.

- Pipeline de Prétraitement : Améliore et normalise les images d'entrée pour une meilleure performance de reconnaissance.

- Recherche Fonctionnelle : Localise efficacement les visages correspondants dans l'ensemble de données.

2. Prérequis

Python 3.8 ou version ultérieure

Bibliothèques nécessaires (voir requirements.txt) :

- OpenCV

- NumPy

- Pandas

- face_recognition

- BM25

- OpenCV-Python

- SciPy

- NLTK

3. Structure du Projet

├── app.py            # Script principal de l'application

├── data.csv          # Métadonnées pour l'ensemble de données

├── dataset.py        # Gestion du chargement et de la gestion de l'ensemble de données

├── preprocess.py     # Fonctions de prétraitement des images d'entrée

├── search.py         # Algorithme de recherche pour la reconnaissance faciale

├── requirements.txt  # Dépendances Python

├── README.md         # Documentation du projet (ce fichier)


4. Ensemble de Données

L'ensemble de données comprend 30 images, chacune correspondant à une personne unique. Chaque image est accompagnée d'une description dans data.csv, qui inclut des informations telles que :

- Noms des fichiers image

- Descriptions des images (ex. : "Homme portant des lunettes", "Femme souriante avec un chapeau", etc.)

- Étiquettes ou ID pour chaque personne

5. Comment Exécuter le Projet

- Cloner le Répertoire :

      git clone <url-du-repertoire>
      cd <dossier-du-repertoire>

- Installer les Dépendances :

      pip install -r requirements.txt

- Préparer l'Ensemble de Données :
Placez les images de l'ensemble de données dans le répertoire data/images et assurez-vous que data.csv correspond aux noms de fichiers, descriptions et étiquettes.

- Exécuter l'Application :

      python app.py

Cela lancera l'application, et vous pourrez interagir avec le système de reconnaissance faciale.

6. Scripts Clés

app.py : Orchestre le flux de travail en intégrant le chargement des données, le prétraitement et la reconnaissance.

dataset.py : Gère le chargement, la gestion et l'augmentation de l'ensemble de données.

preprocess.py : Implémente des fonctions pour redimensionner, normaliser et améliorer les images d'entrée.

search.py : Contient les algorithmes de recherche et de correspondance des visages.

7. Exemple d'Utilisation

Ajouter des Images : Mettez à jour le répertoire "data/images" avec de nouvelles images.

Exécuter la Reconnaissance Faciale :
Utilisez le script "app.py" pour charger l'ensemble de données, prétraiter les images et effectuer la reconnaissance.

Analyser les Résultats :
Consultez les visages reconnus et les métadonnées associées dans la console ou l'interface utilisateur (si implémentée).

8. Améliorations Futures

- Ajouter la prise en charge d'une entrée vidéo en temps réel.

- Améliorer la précision de la reconnaissance avec des ensembles de données plus larges.

- Implémenter une interface utilisateur graphique (GUI) pour une interaction plus facile.

- Ajouter des champs de métadonnées supplémentaires pour des analyses plus riches.

9. Contribution

Les contributions sont les bienvenues ! Veuillez forker le répertoire et soumettre une pull request avec une explication détaillée de vos modifications.

10. Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

