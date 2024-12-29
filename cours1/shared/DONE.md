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
