import qrcode
from PIL import Image, ImageDraw
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

def generer_qr_code_avec_logo(donnees, nom_fichier="qr_avec_logo.png", 
                              chemin_logo=None, couleur_remplissage="black", 
                              couleur_fond="white", taille_logo_ratio=0.3):
    """
    Génère un code QR avec un logo au centre et des couleurs personnalisées
    
    Args:
        donnees (str): Les données à encoder
        nom_fichier (str): Le nom du fichier de sortie
        chemin_logo (str): Chemin vers l'image du logo
        couleur_remplissage (str): Couleur des cases du QR code
        couleur_fond (str): Couleur de fond
        taille_logo_ratio (float): Ratio de la taille du logo par rapport au QR code (0.1 à 0.4)
    
    Returns:
        str: Le chemin du fichier créé
    """
    # Utiliser un niveau de correction d'erreur élevé pour compenser le logo
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Correction élevée
        box_size=10,
        border=4,
    )
    
    qr.add_data(donnees)
    qr.make(fit=True)
    
    # Créer l'image du QR code avec couleurs personnalisées
    img = qr.make_image(fill_color=couleur_remplissage, back_color=couleur_fond)
    
    # Ajouter le logo si fourni
    if chemin_logo and os.path.exists(chemin_logo):
        logo = Image.open(chemin_logo)
        
        # Calculer la taille du logo
        qr_width, qr_height = img.size
        logo_size = int(min(qr_width, qr_height) * taille_logo_ratio)
        
        # Redimensionner le logo
        logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
        
        # Créer un masque rond pour le logo (optionnel)
        mask = Image.new('L', (logo_size, logo_size), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, logo_size, logo_size), fill=255)
        
        # Convertir le logo en RGBA si nécessaire
        if logo.mode != 'RGBA':
            logo = logo.convert('RGBA')
        
        # Appliquer le masque rond
        logo.putalpha(mask)
        
        # Calculer la position centrale
        logo_pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
        
        # Coller le logo sur le QR code
        img.paste(logo, logo_pos, logo)
        
        print(f"Logo ajouté depuis : {chemin_logo}")
    
    # Sauvegarder l'image
    chemin_fichier = os.path.join(os.getcwd(), nom_fichier)
    img.save(chemin_fichier)
    
    print(f"Code QR avec logo généré : {chemin_fichier}")
    return chemin_fichier

def generer_qr_code_avec_logo_existant(donnees, nom_fichier="qr_avec_logo_perso.png", 
                                      chemin_logo_existant=None, couleur_remplissage="black", 
                                      couleur_fond="white", taille_logo_ratio=0.25):
    """
    Génère un code QR avec un logo existant (votre propre image)
    
    Args:
        donnees (str): Les données à encoder
        nom_fichier (str): Le nom du fichier de sortie
        chemin_logo_existant (str): Chemin vers votre image/logo existant
        couleur_remplissage (str): Couleur des cases du QR code
        couleur_fond (str): Couleur de fond
        taille_logo_ratio (float): Ratio de la taille du logo (0.1 à 0.4)
    
    Returns:
        str: Le chemin du fichier créé
    """
    if not chemin_logo_existant or not os.path.exists(chemin_logo_existant):
        print("⚠️  Fichier logo non trouvé. Génération d'un QR code sans logo.")
        return generer_qr_code_personnalise(donnees, nom_fichier, couleur_remplissage, couleur_fond)
    
    return generer_qr_code_avec_logo(donnees, nom_fichier, chemin_logo_existant, 
                                   couleur_remplissage, couleur_fond, taille_logo_ratio)

def creer_logo_simple(nom_fichier="logo_simple.png", couleur="red", taille=100):
    """
    Crée un logo simple (cercle coloré) pour les tests
    
    Args:
        nom_fichier (str): Nom du fichier du logo
        couleur (str): Couleur du logo
        taille (int): Taille du logo en pixels
    
    Returns:
        str: Le chemin du fichier créé
    """
    # Créer une image transparente
    img = Image.new('RGBA', (taille, taille), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    # Dessiner un cercle coloré
    margin = 10
    draw.ellipse([margin, margin, taille-margin, taille-margin], 
                fill=couleur, outline="white", width=3)
    
    # Ajouter une petite étoile au centre
    center = taille // 2
    star_size = 15
    points = []
    for i in range(10):
        angle = i * 36 * 3.14159 / 180
        if i % 2 == 0:
            radius = star_size
        else:
            radius = star_size // 2
        x = center + radius * (angle**0.5 % 1)  # Approximation simple
        y = center + radius * ((angle*2)**0.5 % 1)
        points.extend([x, y])
    
    # Dessiner un petit cercle au centre à la place de l'étoile complexe
    draw.ellipse([center-8, center-8, center+8, center+8], 
                fill="white", outline=couleur, width=2)
    
    chemin_fichier = os.path.join(os.getcwd(), nom_fichier)
    img.save(chemin_fichier)
    
    print(f"Logo simple créé : {chemin_fichier}")
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
    print("=== Générateur de Code QR Avancé ===\n")
    
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
    
    # Exemple 5: Créer un logo simple pour les tests
    logo_path = creer_logo_simple("logo_test.png", "red", 80)
    
    # Exemple 6: QR code avec logo et couleurs personnalisées
    generer_qr_code_avec_logo(
        "QR Code avec logo rouge !",
        "qr_avec_logo_rouge.png",
        chemin_logo=logo_path,
        couleur_remplissage="darkgreen",
        couleur_fond="lightyellow",
        taille_logo_ratio=0.25
    )
    
    # Exemple 7: QR code avec logo bleu
    logo_bleu = creer_logo_simple("logo_bleu.png", "blue", 80)
    generer_qr_code_avec_logo(
        "https://github.com/FleurAccacia",
        "qr_github_avec_logo.png",
        chemin_logo=logo_bleu,
        couleur_remplissage="navy",
        couleur_fond="lightcyan",
        taille_logo_ratio=0.3
    )
    
    # Exemple 8: QR code violet avec logo doré
    logo_dore = creer_logo_simple("logo_dore.png", "gold", 60)
    generer_qr_code_avec_logo(
        "Code QR premium avec logo doré",
        "qr_premium.png",
        chemin_logo=logo_dore,
        couleur_remplissage="purple",
        couleur_fond="lavender",
        taille_logo_ratio=0.2
    )
    
    # Exemple 9: QR code interactif - demander à l'utilisateur
    print("\n--- Mode interactif ---")
    print("Choisissez le type de QR code :")
    print("1. QR code simple")
    print("2. QR code avec couleurs personnalisées")
    print("3. QR code avec logo")
    
    choix = input("Votre choix (1-3) : ")
    donnees_utilisateur = input("Entrez le texte/URL à encoder : ")
    nom_fichier_utilisateur = input("Entrez le nom du fichier (avec .png) : ")
    
    if not nom_fichier_utilisateur.endswith('.png'):
        nom_fichier_utilisateur += '.png'
    
    if choix == "1":
        generer_qr_code(donnees_utilisateur, nom_fichier_utilisateur)
    elif choix == "2":
        couleur_qr = input("Couleur du QR code (ex: red, blue, #FF0000) : ") or "black"
        couleur_bg = input("Couleur de fond (ex: white, yellow, #FFFF00) : ") or "white"
        generer_qr_code_personnalise(donnees_utilisateur, nom_fichier_utilisateur, 
                                    couleur_qr, couleur_bg)
    elif choix == "3":
        # Créer un logo personnalisé
        couleur_logo = input("Couleur du logo (ex: red, blue, green) : ") or "red"
        logo_perso = creer_logo_simple("logo_utilisateur.png", couleur_logo, 80)
        
        couleur_qr = input("Couleur du QR code : ") or "black"
        couleur_bg = input("Couleur de fond : ") or "white"
        
        generer_qr_code_avec_logo(donnees_utilisateur, nom_fichier_utilisateur,
                                 logo_perso, couleur_qr, couleur_bg, 0.25)
    
    print(f"\n🎉 Tous les codes QR ont été générés dans : {os.getcwd()}")
    print("\n📁 Fichiers créés :")
    for fichier in os.listdir('.'):
        if fichier.endswith('.png'):
            print(f"   📷 {fichier}")

if __name__ == "__main__":
    main()