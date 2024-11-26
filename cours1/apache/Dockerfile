# Utiliser l'image officielle d'Apache
FROM httpd:latest

# Copie de la configuration d'Apache pour accepter un ServerName (facultatif)
RUN echo "ServerName localhost" >> /usr/local/apache2/conf/httpd.conf

# Exposer le port 80
EXPOSE 80

# Ne rien faire dans le conteneur (car l'index.html sera monté avec un volume)
CMD ["httpd-foreground"]
