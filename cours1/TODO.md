## TODO

1. Créer une image Docker avec un volume hôte partagé entre Apache et mon script, permettant d'afficher un fichier `index.html` dans le navigateur.

   Après l'installation et l'exécution de l'image Apache, lorsque j'essaie d'accéder à la page `index.html`, j'obtiens une erreur 500 indiquant qu'Apache ne parvient pas à déterminer un nom de domaine complet (FQDN - Fully Qualified Domain Name) pour le serveur.

2. Créer une image Docker qui contiendra un script vérifiant si mon dépôt GitHub contient des modifications. Si c'est le cas, le script devra effectuer un `git pull` pour mettre à jour le fichier `index.html` dans le volume hôte.
