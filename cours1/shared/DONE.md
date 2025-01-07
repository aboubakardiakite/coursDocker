## Ce que j'ai fait pour résoudre le problème

1 - creation de l'image DOcker de mon serveur Apache
```code
docker build -f Dockerfile.server -t my-apache .
```

2 - creation de l'image Docker de mon script de synchronisation
```code
docker build -f Dockerfile.git-puller -t git-sync .
```

3 - creation d'un volume partagé avec Docker
```code
docker volume create shared_volume
```
4 - Creation de l'image Docker du serveur SMTP
```code
Docker build -f Dockerfile.smtp -t smtp-notify .
```

5 - Lancement du conteneur Apache
```code
docker run -d --name apache-server -p 8080:8080 -v shared_volume:/usr/local/apache2/htdocs my-apache
```

6 - Lancement du conteneur du script de synchronisation

```code
docker run -d --name git-sync -v shared_volume:/shared --env-file .env git-sync
```

7 - Verification des logs du conteneur
```code

docker logs git-sync
```


8 - Verification du fichier `index.html` dans le volume partagé
```code
docker exec apache-server cat /usr/local/apache2/htdocs/index.html
```

9 - Lancement du conteneur du serveur SMTP
```code
docker run -d --name smtp-notifier -v shared_volume:/shared --env-file .env smtp-notify
```

10 - Verification des logs du conteneur SMTP
```code
docker logs smtp-notifier
```

11 - Verification que le fichier index.html est bien mis a jour a chaque fois que le dossier partagé est modifié
```code
docker exec apache-server cat /usr/local/apache2/htdocs/index.html
```

