## Les commandes docker utiliser

Ces commandes doivent être exécutées dans le répertoire `docker`.

### Utilisation de docker-compose

Utilisez docker-compose pour simplifier le processus de création et de gestion des conteneurs.
Pour cela, vous pouvez exécuter la commande suivante :

```code
docker-compose up -d
```

Pour arrêter les conteneurs, utilisez la commande :

```code
docker-compose down --volumes --rmi all
```

### Creations manuelles des conteneurs


1- creer les images 

Ce placer dans le dossier docker

```code
docker build -f Dockerfile.server -t my-apache .
docker build -f Dockerfile.git-puller -t git-sync .
docker build -f Dockerfile.smtp -t smtp-notify .
```

2- Creer un volume partagé avec docker

```code
docker volume create shared_volume
```

3- Lancer le conteneur Apache

```code
docker run -d --name apache-server -p 8080:8080 -v shared_volume:/usr/local/apache2/htdocs my-apache
```

4- Lancer le conteneur du script de synchronisation

```code
docker run -d --name git-sync -v shared_volume:/shared --env-file .env git-sync
```

5- Vérifier les logs du conteneur

```code
docker logs git-sync
```

6- Vérifier le fichier `index.html` dans le volume partagé

```code
docker exec apache-server cat /usr/local/apache2/htdocs/index.html
```


7- Lancer le conteneur du serveur SMTP

```code
docker run -d   --name smtp-notifier   -v shared_volume:/shared   --env-file .env   smtp-notify
```

8- Vérifier les logs du conteneur SMTP

```code
docker logs smtp-notifier
```
