## TODO

1. Créer une image Docker avec un volume hôte partagé entre Apache et mon script, permettant d'afficher un fichier `index.html` dans le navigateur.

   Après l'installation et l'exécution de l'image Apache, lorsque j'essaie d'accéder à la page `index.html`, j'obtiens une erreur 500 indiquant qu'Apache ne parvient pas à déterminer un nom de domaine complet (FQDN - Fully Qualified Domain Name) pour le serveur.

2. Créer une image Docker qui contiendra un script vérifiant si mon dépôt GitHub contient des modifications. Si c'est le cas, le script devra effectuer un `git pull` pour mettre à jour le fichier `index.html` dans le volume hôte. 

3. Creer un image Docker pour le serveur SMTP
   Pour envoyer un mail a chaque fois que le dossier partagé est modifié

4. Faire un script qui envoie un mail a chaque fois que le dossier partagé est modifié
   Pour cela, il faut installer un serveur SMTP dans un conteneur Docker et configurer le script pour envoyer un mail à chaque modification du dossier partagé.

5. Creer un volume partagé entre les 3 conteneurs
   Le volume partagé doit être monté sur le dossier `/shared` de chaque conteneur.

6. Lancer les 3 conteneurs
   Pour cela, il faut lancer les conteneurs Apache, Git Sync et SMTP Notifier en utilisant le volume partagé créé précédemment.

7. Verifier que le fichier index.html est bien mis a jour a chaque fois que le dossier partagé est modifié

8. Verifier que le serveur SMTP envoie bien un mail a chaque fois que le dossier partagé est modifié

9. Mettre a jour le fichier README.md avec les nouvelles commandes Docker
