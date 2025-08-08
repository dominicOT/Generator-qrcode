#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de test rapide pour les codes QR avec logos et couleurs
"""

from qrCode import generer_qr_code_avec_logo, creer_logo_simple, generer_qr_code_personnalise

def test_rapide():
    """
    Test rapide des nouvelles fonctionnalités
    """
    print("🧪 Test des nouvelles fonctionnalités...\n")
    
    # 1. Code QR avec couleurs personnalisées
    print("1️⃣  Code QR rouge sur fond jaune...")
    generer_qr_code_personnalise(
        "Test couleurs personnalisées",
        "test_couleurs.png",
        couleur_remplissage="red",
        couleur_fond="yellow"
    )
    
    # 2. Créer un logo simple
    print("\n2️⃣  Création d'un logo vert...")
    logo_path = creer_logo_simple("logo_vert.png", "green", 80)
    
    # 3. Code QR avec logo
    print("\n3️⃣  Code QR bleu avec logo vert...")
    generer_qr_code_avec_logo(
        "https://github.com/FleurAccacia/Generator-qrcode",
        "test_avec_logo.png",
        chemin_logo=logo_path,
        couleur_remplissage="blue",
        couleur_fond="lightblue",
        taille_logo_ratio=0.3
    )
    
    # 4. Code QR avec votre image existante (si elle existe)
    print("\n4️⃣  Test avec image existante...")
    if input("Avez-vous une image à utiliser comme logo ? (y/n): ").lower() == 'y':
        chemin_image = input("Entrez le chemin de votre image : ")
        couleur_qr = input("Couleur du QR code (ex: purple): ") or "purple"
        couleur_bg = input("Couleur de fond (ex: pink): ") or "pink"
        
        from qrCode import generer_qr_code_avec_logo_existant
        generer_qr_code_avec_logo_existant(
            "Mon QR code personnalisé !",
            "qr_avec_mon_logo.png",
            chemin_image,
            couleur_qr,
            couleur_bg,
            0.25
        )
    
    print("\n✅ Tests terminés ! Vérifiez les fichiers générés.")

if __name__ == "__main__":
    test_rapide()
