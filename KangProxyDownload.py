# Importer le module requests pour les requêtes HTTP
import requests

# Définir les URL des fichiers de proxies et le nom du dossier de sortie
urls_fichiers = {
    "http": "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt",
    "https": "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt",
    "socks4": "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks4/socks4.txt",
    "socks5": "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks5/socks5.txt",
}

# Définir le nom du dossier de sortie
nom_dossier_sortie = "KangProxy"

# Créer le dossier de sortie s'il n'existe pas
import os
if not os.path.exists(nom_dossier_sortie):
    os.makedirs(nom_dossier_sortie)

# Télécharger chaque fichier de proxy
for type_proxy, url_fichier in urls_fichiers.items():
    nom_fichier_sortie = f"{nom_dossier_sortie}/{type_proxy}.txt"

    # Envoyer une requête GET à l'URL du fichier de proxies
    response = requests.get(url_fichier, stream=True)

    # Si la requête est réussie
    if response.status_code == 200:

        # Déterminer la taille du fichier
        taille_fichier = int(response.headers.get("Content-Length", 0))

        # Afficher un message de début de téléchargement
        print(f"Téléchargement du fichier {nom_fichier_sortie} ({taille_fichier} octets)...")

        # Télécharger le fichier en affichant la progression
        with open(nom_fichier_sortie, "wb") as fichier:
            for chunk in response.iter_content(chunk_size=8192):
                fichier.write(chunk)
                # Afficher la progression
                print(f"\r{fichier.tell()}/{taille_fichier} octets téléchargés", end="")

        # Afficher un message de succès
        print("\nTéléchargement du fichier {nom_fichier_sortie} terminé avec succès.")

    else:
        # Afficher un message d'erreur
        print(f"Echec du téléchargement du fichier {nom_fichier_sortie}.")

