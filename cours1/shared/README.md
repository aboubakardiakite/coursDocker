# Projet : Gestion et Surveillance de Fichiers avec Docker

Ce projet combine plusieurs fonctionnalités essentielles pour gérer un répertoire partagé, surveiller ses modifications, synchroniser les fichiers avec Git, et configurer un serveur SMTP et Apache. Le tout est orchestré via Docker pour une gestion simplifiée.

---

## Structure du Projet

```plaintext
docker/
├── .env                      # Fichier d'environnement pour les variables sensibles
├── Dockerfile.git-puller     # Dockerfile pour la synchronisation Git
├── Dockerfile.server         # Dockerfile pour le serveur Apache
├── Dockerfile.smtp           # Dockerfile pour l'envoi de notifications SMTP
├── git-pull.sh               # Script shell pour le pull Git automatique
├── index.html                # Page d'accueil pour le serveur Apache
├── notify_changes.py         # Script Python pour surveiller les modifications dans un répertoire
shared/
├── Docker.md                 # Documentation Docker
├── DONE.md                   # Liste des tâches terminées
├── README.md                 # Documentation principale
└── TODO.md                   # Liste des tâches à effectuer

```

## Prérequis

- **Docker**  
  Nécessaires pour exécuter les différents conteneurs (serveur Apache, synchronisation Git, notifications SMTP).

- **Accès à un service SMTP**  
  Par exemple, Gmail pour l'envoi des notifications par e-mail.



## Fonctionnalités

### Surveillance de fichiers
- Le script `notify_changes.py` surveille les modifications dans un répertoire partagé (`shared`) :
  - **Création de fichiers.**
  - **Suppression de fichiers.**
  - **Modification des fichiers** (y compris leur taille).
- Envoie des notifications par e-mail via un serveur SMTP.

### Synchronisation Git
- Le script `git-pull.sh` permet de synchroniser automatiquement le contenu du répertoire partagé avec un dépôt Git.
- Hébergé dans un conteneur Docker via le `Dockerfile.git-puller`.

### Serveur Apache
- Le `Dockerfile.server` configure un serveur Apache pour servir les fichiers du répertoire `shared`.
- Inclut une page d'accueil personnalisée (`index.html`).

### Notifications SMTP
- Le `Dockerfile.smtp` contient la configuration pour envoyer des notifications par e-mail en cas de modification dans le répertoire.

## Dockerfiles

- **Dockerfile.git-puller** : Synchronise le répertoire partagé avec le dépôt Git.
- **Dockerfile.server** : Configure le serveur Apache pour servir les fichiers.
- **Dockerfile.smtp** : Configure l'environnement pour envoyer des e-mails.

## Fichiers Importants

- **notify_changes.py**  
  Ce script utilise la bibliothèque Watchdog pour surveiller les changements dans le répertoire partagé. Lorsqu'un changement est détecté, il envoie une notification par e-mail en utilisant yagmail.

- **git-pull.sh**  
  Ce script synchronise le contenu local du répertoire partagé avec un dépôt Git distant.

- **index.html**  
  Page personnalisée pour le serveur Apache. 




