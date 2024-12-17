## Instructions

### Informations à stocker pour chaque chanson :

- **Titre** : le nom de la chanson.
- **Artiste** : l'auteur ou interprète de la chanson.
- **Catégorie** : le genre musical (exemple : pop, rock, classique).
- **Score** : une note sur 5 attribuée à la chanson.

### Fonctionnalités du programme :

1. **Création et gestion du fichier JSON** :

   - Le programme doit ouvrir automatiquement un fichier nommé `music.json` lors de son démarrage.
   - Si le fichier n'existe pas, il doit être créé automatiquement à la racine du programme.
   - Le fichier contiendra la liste des chansons enregistrées.

2. **Création de la classe `Chanson`** :

   - Cette classe doit inclure des attributs pour le titre, l'artiste, la catégorie et le score.
   - Ajouter une méthode permettant de retourner une représentation textuelle de la chanson.

3. **Gestion des chansons** :

   - **Ajout** : Permettre à l'utilisateur d'ajouter une nouvelle chanson.
   - **Affichage** : Lister toutes les chansons enregistrées dans le fichier.
   - **Modification** : Modifier les informations d'une chanson existante.
   - **Suppression** : Supprimer une chanson de la liste.

4. **Sauvegarde des données** :
   - Les modifications doivent être enregistrées en temps réel dans le fichier JSON.

### Contraintes techniques :

- Utiliser des structures conditionnelles et des boucles pour gérer les interactions utilisateur.
- Manipuler le module `json` pour gérer le fichier.
- un menu pour que l'utilisateur puisse choisir d'ajouter, modifier, supprimer ou afficher les chansons.
