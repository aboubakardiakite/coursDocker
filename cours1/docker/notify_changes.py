import os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import yagmail

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),  # Afficher dans la console
        logging.FileHandler("file_changes.log")  # Enregistrer dans un fichier log
    ]
)

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")

if not EMAIL_ADDRESS or not EMAIL_PASSWORD or not TO_EMAIL:
    logging.critical("Les variables d'environnement EMAIL_ADDRESS, EMAIL_PASSWORD et TO_EMAIL doivent être définies.")
    raise ValueError("Les variables d'environnement EMAIL_ADDRESS, EMAIL_PASSWORD et TO_EMAIL doivent être définies.")

WATCHED_DIR = "/shared"
if not os.path.exists(WATCHED_DIR):
    logging.critical(f"Le répertoire surveillé n'existe pas : {WATCHED_DIR}")
    raise FileNotFoundError(f"Le répertoire surveillé n'existe pas : {WATCHED_DIR}")

file_sizes = {}

class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return

        file_path = event.src_path
        file_name = os.path.basename(file_path)

        try:
            # Obtenir la nouvelle taille du fichier
            new_size = os.path.getsize(file_path)
            old_size = file_sizes.get(file_path, None)

            if old_size is None:
                file_sizes[file_path] = new_size
                logging.info(f"Nouveau fichier suivi : {file_name} avec taille {new_size} octets.")
            elif new_size != old_size:
                file_sizes[file_path] = new_size  # Mise à jour de la taille
                subject = f"Taille modifiée : {file_name}"
                body = f"Le fichier {file_name} a été modifié : {old_size} → {new_size} octets."
                logging.info(body)
                send_email(subject, body)
        except FileNotFoundError:
            logging.warning(f"Le fichier {file_name} a été supprimé avant de vérifier sa taille.")

    def on_deleted(self, event):
        if event.is_directory:
            return

        file_path = event.src_path
        file_name = os.path.basename(file_path)

        if file_path in file_sizes:
            del file_sizes[file_path]  # Retirer du suivi
            subject = f"Fichier supprimé : {file_name}"
            body = f"Le fichier suivant a été supprimé : {file_name}"
            logging.info(body)
            send_email(subject, body)

def send_email(subject, body):
    try:
        yag = yagmail.SMTP(EMAIL_ADDRESS, EMAIL_PASSWORD)
        yag.send(to=TO_EMAIL, subject=subject, contents=body)
        logging.info(f"E-mail envoyé : {subject}")
    except Exception as e:
        logging.error(f"Erreur lors de l'envoi de l'e-mail : {e}")

if __name__ == "__main__":
    logging.info(f"Surveillance du répertoire : {WATCHED_DIR}")
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, WATCHED_DIR, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("Arrêt de la surveillance.")
        observer.stop()
    observer.join()
