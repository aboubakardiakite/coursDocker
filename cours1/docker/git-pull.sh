#!/bin/bash

# Répertoire où le repository sera cloné
REPO_DIR="/tmp/repo"


# Récupérer le token et l'URL du repository
REPO_URL="https://$GITHUB_TOKEN@github.com/aboubakardiakite/docker.git"



# Créer le répertoire s'il n'existe pas
mkdir -p "$REPO_DIR"

# Cloner le repository s'il n'est pas déjà présent
if [ ! -d "$REPO_DIR/.git" ]; then
    git clone $REPO_URL $REPO_DIR
fi

# Naviguer dans le répertoire du repo
cd $REPO_DIR || exit 1

# Boucle infinie pour vérifier les mises à jour toutes les 10 secondes
while true; do
    # Vérifier les changements et faire un pull
    git fetch --all
    git reset --hard origin/main

    # Copier le contenu dans le volume partagé
    cp -r $REPO_DIR/* /shared/

    # Attendre 10 secondes avant de vérifier à nouveau
    sleep 10
done
