import qrcode
from PIL import Image
import os

def generer_qr_code(donnees, nom_fichier="qr_code.png", taille=10, bordure=4):
    """
    Génère un code QR à partir des données fournies
    
    Args:
        donnees (str): Les données à encoder dans le QR code
        nom_fichier (str): Le nom du fichier de sortie
        taille (int): La taille des cases du QR code
        bordure (int): La taille de la bordure
    
    Returns:
        str: Le chemin du fichier créé
    """
    # Créer l'objet QR code
    qr = qrcode.QRCode(
        version=1,  # Contrôle la taille du QR Code (1 est le plus petit)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Niveau de correction d'erreur
        box_size=taille,  # Taille de chaque case
        border=bordure,  # Taille de la bordure
    )
    
    # Ajouter les données
    qr.add_data(donnees)
    qr.make(fit=True)
    
    # Créer l'image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Sauvegarder l'image
    chemin_fichier = os.path.join(os.getcwd(), nom_fichier)
    img.save(chemin_fichier)
    
    print(f"Code QR généré avec succès : {chemin_fichier}")
    return chemin_fichier

def generer_qr_code_personnalise(donnees, nom_fichier="qr_code_personnalise.png", 
                                couleur_remplissage="black", couleur_fond="white"):
    """
    Génère un code QR avec des couleurs personnalisées
    
    Args:
        donnees (str): Les données à encoder
        nom_fichier (str): Le nom du fichier de sortie
        couleur_remplissage (str): Couleur des cases du QR code
        couleur_fond (str): Couleur de fond
    
    Returns:
        str: Le chemin du fichier créé
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    
    qr.add_data(donnees)
    qr.make(fit=True)
    
    # Créer l'image avec des couleurs personnalisées
    img = qr.make_image(fill_color=couleur_remplissage, back_color=couleur_fond)
    
    chemin_fichier = os.path.join(os.getcwd(), nom_fichier)
    img.save(chemin_fichier)
    
    print(f"Code QR personnalisé généré : {chemin_fichier}")
    return chemin_fichier

def main():
    """
    Fonction principale - exemples d'utilisation
    """
    print("=== Générateur de Code QR ===\n")
    
    # Exemple 1: QR code simple avec du texte
    texte = "Bonjour, ceci est un test de code QR !"
    generer_qr_code(texte, "qr_texte.png")
    
    # Exemple 2: QR code avec une URL
    url = "https://www.github.com"
    generer_qr_code(url, "qr_url.png")
    
    # Exemple 3: QR code avec des coordonnées géographiques
    coordonnees = "geo:48.8566,2.3522"  # Paris
    generer_qr_code(coordonnees, "qr_coordonnees.png")
    
    # Exemple 4: QR code personnalisé avec des couleurs
    generer_qr_code_personnalise(
        "Code QR coloré !",
        "qr_colore.png",
        couleur_remplissage="darkblue",
        couleur_fond="lightgray"
    )
    
    # Exemple 5: QR code interactif - demander à l'utilisateur
    print("\n--- Mode interactif ---")
    donnees_utilisateur = input("Entrez le texte/URL à encoder dans le QR code : ")
    nom_fichier_utilisateur = input("Entrez le nom du fichier (avec .png) : ")
    
    if not nom_fichier_utilisateur.endswith('.png'):
        nom_fichier_utilisateur += '.png'
    
    generer_qr_code(donnees_utilisateur, nom_fichier_utilisateur)
    
    print(f"\nTous les codes QR ont été générés dans le répertoire : {os.getcwd()}")

if __name__ == "__main__":
    main()