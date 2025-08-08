#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test automatisé pour reproduire le problème de dégradé
"""

from qrCode import *

def test_automatique():
    """
    Test automatisé des dégradés sans interaction utilisateur
    """
    print("🧪 Test automatisé des dégradés")
    print("=" * 50)
    
    # Test 1: QR simple avec dégradé (sans logo)
    print("\n1️⃣ Test QR avec dégradé sans logo")
    try:
        resultat = creer_degraded_qr(
            "https://github.com/FleurAccacia", 
            "auto_test_degrade.png", 
            "red", 
            "blue", 
            "white"
        )
        print(f"   ✅ Succès: {resultat}")
    except Exception as e:
        print(f"   ❌ Erreur: {e}")
    
    # Test 2: QR avec dégradé et logo simple
    print("\n2️⃣ Test QR avec dégradé et logo")
    try:
        # Créer un logo d'abord
        logo = creer_logo_simple("auto_logo.png", "white", 80)
        
        # Créer QR avec dégradé et logo
        resultat = generer_qr_code_avec_logo_et_degrade(
            "Test avec logo et dégradé",
            "auto_test_logo_degrade.png",
            logo,
            "purple",
            "pink",
            "lightgray",
            0.25
        )
        print(f"   ✅ Succès: {resultat}")
    except Exception as e:
        print(f"   ❌ Erreur: {e}")
    
    # Test 3: Simulation complète du workflow utilisateur
    print("\n3️⃣ Test workflow complet")
    try:
        # Simuler la saisie utilisateur
        donnees = "https://example.com"
        nom_fichier = "auto_test_workflow.png"
        
        # Simuler choix couleur avec virgule
        couleur_entree = "darkgreen,lightgreen"
        couleur_validee = valider_couleur(couleur_entree)
        
        print(f"   Couleur entrée: {couleur_entree}")
        print(f"   Couleur validée: {couleur_validee}")
        print(f"   Type: {type(couleur_validee)}")
        
        if isinstance(couleur_validee, list):
            print(f"   Création dégradé {couleur_validee[0]} → {couleur_validee[1]}")
            resultat = creer_degraded_qr(
                donnees, 
                nom_fichier, 
                couleur_validee[0], 
                couleur_validee[1], 
                "white"
            )
            print(f"   ✅ Workflow réussi: {resultat}")
        else:
            print(f"   ❌ Couleur non reconnue comme liste")
            
    except Exception as e:
        print(f"   ❌ Erreur workflow: {e}")
    
    # Test 4: Test avec couleurs hex
    print("\n4️⃣ Test avec couleurs hexadécimales")
    try:
        couleur_hex = "#FF0000,#FFA500"  # Rouge vers orange
        couleur_validee = valider_couleur(couleur_hex)
        
        print(f"   Couleur hex: {couleur_hex}")
        print(f"   Validée: {couleur_validee}")
        
        if isinstance(couleur_validee, list):
            resultat = creer_degraded_qr(
                "Test couleurs hex",
                "auto_test_hex.png",
                couleur_validee[0],
                couleur_validee[1],
                "white"
            )
            print(f"   ✅ Hex réussi: {resultat}")
        else:
            print(f"   ❌ Hex non validé")
            
    except Exception as e:
        print(f"   ❌ Erreur hex: {e}")
    
    print("\n" + "=" * 50)
    print("🎯 Tests automatisés terminés!")

if __name__ == "__main__":
    test_automatique()
