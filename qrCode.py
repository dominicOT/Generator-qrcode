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

def afficher_propositions_couleurs():
    """
    Affiche les propositions de couleurs disponibles
    """
    print("\n🎨 Propositions de couleurs :")
    print("1. Noir (black)")
    print("2. Bleu foncé (darkblue)")
    print("3. Vert foncé (darkgreen)")
    print("4. Rouge (red)")
    print("5. Violet (purple)")
    print("6. Orange foncé (darkorange)")
    print("7. Marron (brown)")
    print("8. Personnalisée (tapez votre couleur)")

def valider_couleur(couleur):
    """
    Valide qu'une couleur est correcte et retourne la liste des couleurs
    """
    try:
        # Nettoyer la couleur et séparer les couleurs multiples
        couleurs = [c.strip() for c in couleur.split(',')]
        
        # Tester chaque couleur avec PIL
        from PIL import ImageColor
        couleurs_validees = []
        for c in couleurs:
            if c:  # Ignorer les chaînes vides
                ImageColor.getrgb(c)  # Test de validation
                couleurs_validees.append(c)
        
        if len(couleurs_validees) == 1:
            return couleurs_validees[0]  # Une seule couleur
        elif len(couleurs_validees) >= 2:
            return couleurs_validees[:2]  # Maximum 2 couleurs pour le dégradé
        else:
            return None
    except:
        return None

def creer_degraded_qr(donnees, nom_fichier, couleur1, couleur2, couleur_fond="white"):
    """
    Crée un QR code avec dégradé entre deux couleurs
    """
    from PIL import ImageColor
    
    # Créer le QR code de base
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    
    qr.add_data(donnees)
    qr.make(fit=True)
    
    # Créer l'image de base en noir et blanc
    img_base = qr.make_image(fill_color="black", back_color="white")
    width, height = img_base.size
    
    # Créer une nouvelle image en mode RGB
    img = Image.new('RGB', (width, height), ImageColor.getrgb(couleur_fond))
    
    # Convertir les couleurs en RGB
    rgb1 = ImageColor.getrgb(couleur1)
    rgb2 = ImageColor.getrgb(couleur2)
    
    # Appliquer le dégradé
    for y in range(height):
        # Calculer le ratio du dégradé (de haut en bas)
        ratio = y / height
        
        # Interpoler entre les deux couleurs
        r = int(rgb1[0] * (1 - ratio) + rgb2[0] * ratio)
        g = int(rgb1[1] * (1 - ratio) + rgb2[1] * ratio)
        b = int(rgb1[2] * (1 - ratio) + rgb2[2] * ratio)
        couleur_degradee = (r, g, b)
        
        for x in range(width):
            # Si le pixel est noir dans l'image de base (partie du QR code)
            if img_base.getpixel((x, y)) == 0:  # 0 = noir
                img.putpixel((x, y), couleur_degradee)
    
    # Sauvegarder
    chemin_fichier = os.path.join(os.getcwd(), nom_fichier)
    img.save(chemin_fichier)
    
    print(f"Code QR avec dégradé {couleur1} → {couleur2} généré : {chemin_fichier}")
    return chemin_fichier

def obtenir_couleur_utilisateur(type_couleur="QR code"):
    """
    Obtient la couleur choisie par l'utilisateur
    """
    afficher_propositions_couleurs()
    print("💡 Astuce: Vous pouvez entrer deux couleurs séparées par une virgule pour un dégradé !")
    print("   Exemple: red, blue ou #FF0000, #0000FF")
    
    choix = input(f"\nChoisissez la couleur pour {type_couleur} (1-8) : ")
    
    couleurs = {
        "1": "black",
        "2": "darkblue", 
        "3": "darkgreen",
        "4": "red",
        "5": "purple",
        "6": "darkorange",
        "7": "brown"
    }
    
    if choix in couleurs:
        return couleurs[choix]
    elif choix == "8":
        while True:
            couleur_perso = input("Entrez votre couleur (ex: #FF0000 ou red,blue pour dégradé) : ").strip()
            if not couleur_perso:
                return "black"
            
            couleur_validee = valider_couleur(couleur_perso)
            if couleur_validee:
                return couleur_validee
            else:
                print("❌ Couleur invalide ! Exemples valides : red, blue, #FF0000, red,blue")
                retry = input("Voulez-vous réessayer ? (o/n) : ").lower()
                if retry != 'o':
                    return "black"
    else:
        print("Choix invalide, utilisation du noir par défaut.")
        return "black"

def generer_qr_code_avec_logo_et_degrade(donnees, nom_fichier, chemin_logo, 
                                        couleur1, couleur2, couleur_fond="white", 
                                        taille_logo_ratio=0.25):
    """
    Génère un QR code avec logo et dégradé
    """
    # D'abord créer le QR avec dégradé
    creer_degraded_qr(donnees, "temp_degrade.png", couleur1, couleur2, couleur_fond)
    
    # Ensuite ajouter le logo
    if chemin_logo and os.path.exists(chemin_logo):
        img = Image.open("temp_degrade.png")
        logo = Image.open(chemin_logo)
        
        # Calculer la taille du logo
        qr_width, qr_height = img.size
        logo_size = int(min(qr_width, qr_height) * taille_logo_ratio)
        
        # Redimensionner le logo
        logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
        
        # Créer un masque rond pour le logo
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
        
        # Sauvegarder le résultat final
        chemin_fichier = os.path.join(os.getcwd(), nom_fichier)
        img.save(chemin_fichier)
        
        # Nettoyer le fichier temporaire
        try:
            os.remove("temp_degrade.png")
        except:
            pass
            
        print(f"QR code avec logo et dégradé {couleur1} → {couleur2} généré : {chemin_fichier}")
        return chemin_fichier
    else:
        # Pas de logo, renommer juste le fichier temporaire
        os.rename("temp_degrade.png", nom_fichier)
        return nom_fichier

def obtenir_couleur_fond():
    """
    Obtient la couleur de fond choisie par l'utilisateur
    """
    print("\n🎨 Propositions de couleurs de fond :")
    print("1. Blanc (white)")
    print("2. Gris clair (lightgray)")
    print("3. Jaune clair (lightyellow)")
    print("4. Bleu clair (lightcyan)")
    print("5. Rose clair (lightpink)")
    print("6. Vert clair (lightgreen)")
    print("7. Personnalisée")
    
    choix = input("\nChoisissez la couleur de fond (1-7) : ")
    
    couleurs_fond = {
        "1": "white",
        "2": "lightgray",
        "3": "lightyellow", 
        "4": "lightcyan",
        "5": "lightpink",
        "6": "lightgreen"
    }
    
    if choix in couleurs_fond:
        return couleurs_fond[choix]
    elif choix == "7":
        while True:
            couleur_perso = input("Entrez votre couleur de fond (ex: #FFFF00, yellow) : ").strip()
            if not couleur_perso:
                return "white"
            
            couleur_validee = valider_couleur(couleur_perso)
            if couleur_validee:
                if isinstance(couleur_validee, list):
                    return couleur_validee[0]  # Prendre la première couleur pour le fond
                return couleur_validee
            else:
                print("❌ Couleur invalide ! Exemples valides : yellow, white, #FFFF00")
                retry = input("Voulez-vous réessayer ? (o/n) : ").lower()
                if retry != 'o':
                    return "white"
    else:
        print("Choix invalide, utilisation du blanc par défaut.")
        return "white"
    """
    Obtient la couleur de fond choisie par l'utilisateur
    """
    print("\n🎨 Propositions de couleurs de fond :")
    print("1. Blanc (white)")
    print("2. Gris clair (lightgray)")
    print("3. Jaune clair (lightyellow)")
    print("4. Bleu clair (lightcyan)")
    print("5. Rose clair (lightpink)")
    print("6. Vert clair (lightgreen)")
    print("7. Personnalisée")
    
    choix = input("\nChoisissez la couleur de fond (1-7) : ")
    
    couleurs_fond = {
        "1": "white",
        "2": "lightgray",
        "3": "lightyellow", 
        "4": "lightcyan",
        "5": "lightpink",
        "6": "lightgreen"
    }
    
    if choix in couleurs_fond:
        return couleurs_fond[choix]
    elif choix == "7":
        while True:
            couleur_perso = input("Entrez votre couleur de fond (ex: #FFFF00, yellow) : ").strip()
            if not couleur_perso:
                return "white"
            
            couleur_validee = valider_couleur(couleur_perso)
            if couleur_validee:
                return couleur_validee
            else:
                print("❌ Couleur invalide ! Exemples valides : yellow, white, #FFFF00")
                retry = input("Voulez-vous réessayer ? (o/n) : ").lower()
                if retry != 'o':
                    return "white"
    else:
        print("Choix invalide, utilisation du blanc par défaut.")
        return "white"

def demander_logo():
    """
    Demande à l'utilisateur s'il veut ajouter un logo
    """
    print("\n📷 Voulez-vous ajouter un logo au milieu du QR code ?")
    print("1. Oui, j'ai mon propre logo")
    print("2. Oui, créer un logo simple")
    print("3. Non, sans logo")
    
    choix = input("\nVotre choix (1-3) : ")
    return choix

def obtenir_chemin_logo():
    """
    Obtient le chemin du logo de l'utilisateur
    """
    chemin = input("\nEntrez le chemin de votre logo (ex: C:/Users/nom/image.png) : ")
    
    if os.path.exists(chemin):
        print(f"✅ Logo trouvé : {chemin}")
        return chemin
    else:
        print("❌ Fichier non trouvé. Création d'un logo simple à la place...")
        couleur = input("Couleur du logo simple (ex: red, blue, green) : ") or "red"
        return creer_logo_simple("logo_utilisateur.png", couleur, 80)

def main():
    """
    Interface utilisateur principale selon la logique demandée
    """
    print("=" * 60)
    print("🎯 GÉNÉRATEUR DE CODE QR - Fleur-Accacia")
    print("=" * 60)
    print("Bienvenue ! Créez votre code QR personnalisé en quelques étapes\n")
    
    # Étape 1: Obtenir les données à encoder
    print("📝 ÉTAPE 1: Contenu du QR Code")
    donnees = input("Entrez le lien ou texte à encoder dans le QR code : ")
    
    if not donnees.strip():
        print("❌ Erreur : Vous devez entrer du contenu !")
        return
    
    # Étape 2: Type de QR code
    print("\n🎨 ÉTAPE 2: Type de QR Code")
    print("1. QR Code simple (noir et blanc)")
    print("2. QR Code avec couleurs personnalisées")
    
    type_qr = input("\nVotre choix (1 ou 2) : ")
    
    # Nom du fichier
    nom_fichier = input("\n📁 Nom du fichier (sans extension) : ") or "mon_qr_code"
    if not nom_fichier.endswith('.png'):
        nom_fichier += '.png'
    
    if type_qr == "1":
        # QR Code simple
        print("\n✨ Vous avez choisi un QR Code simple")
        
        # Demander logo
        choix_logo = demander_logo()
        
        if choix_logo == "1":
            # Logo utilisateur
            chemin_logo = obtenir_chemin_logo()
            generer_qr_code_avec_logo(donnees, nom_fichier, chemin_logo, 
                                    "black", "white", 0.25)
        elif choix_logo == "2":
            # Logo simple
            couleur_logo = input("\nCouleur du logo simple : ") or "red"
            logo = creer_logo_simple("logo_temp.png", couleur_logo, 80)
            generer_qr_code_avec_logo(donnees, nom_fichier, logo, 
                                    "black", "white", 0.25)
        else:
            # Sans logo
            generer_qr_code(donnees, nom_fichier)
    
    elif type_qr == "2":
        # QR Code avec couleurs
        print("\n🌈 Vous avez choisi un QR Code coloré")
        
        # Choisir couleurs
        print("\n🎨 ÉTAPE 3: Choix des couleurs")
        couleur_qr = obtenir_couleur_utilisateur("le QR code")
        couleur_fond = obtenir_couleur_fond()
        
        # Demander logo
        choix_logo = demander_logo()
        
        if choix_logo == "1":
            # Logo utilisateur
            chemin_logo = obtenir_chemin_logo()
            if isinstance(couleur_qr, list):
                # Dégradé avec logo
                generer_qr_code_avec_logo_et_degrade(donnees, nom_fichier, chemin_logo,
                                                   couleur_qr[0], couleur_qr[1], couleur_fond, 0.25)
            else:
                # Couleur unique avec logo
                generer_qr_code_avec_logo(donnees, nom_fichier, chemin_logo, 
                                        couleur_qr, couleur_fond, 0.25)
        elif choix_logo == "2":
            # Logo simple
            couleur_logo = input("\nCouleur du logo simple : ") or "white"
            logo = creer_logo_simple("logo_temp.png", couleur_logo, 80)
            if isinstance(couleur_qr, list):
                # Dégradé avec logo simple
                generer_qr_code_avec_logo_et_degrade(donnees, nom_fichier, logo,
                                                   couleur_qr[0], couleur_qr[1], couleur_fond, 0.25)
            else:
                # Couleur unique avec logo simple
                generer_qr_code_avec_logo(donnees, nom_fichier, logo, 
                                        couleur_qr, couleur_fond, 0.25)
        else:
            # Sans logo - vérifier si c'est un dégradé
            if isinstance(couleur_qr, list):
                # Dégradé avec deux couleurs
                creer_degraded_qr(donnees, nom_fichier, couleur_qr[0], couleur_qr[1], couleur_fond)
            else:
                # Couleur unique
                generer_qr_code_personnalise(donnees, nom_fichier, couleur_qr, couleur_fond)
    
    else:
        print("❌ Choix invalide. Génération d'un QR code simple par défaut.")
        generer_qr_code(donnees, nom_fichier)
    
    # Message de fin
    print("\n" + "=" * 60)
    print("🎉 FÉLICITATIONS !")
    print(f"✅ Votre QR Code a été généré avec succès : {nom_fichier}")
    print(f"📁 Emplacement : {os.getcwd()}")
    print("\n� Merci d'avoir généré votre code QR chez Fleur-Accacia !")
    print("🌟 N'hésitez pas à revenir pour créer d'autres codes QR")
    print("=" * 60)

if __name__ == "__main__":
    main()