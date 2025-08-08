#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test de débogage pour les dégradés
"""

from qrCode import *

def tester_degrades():
    """
    Teste les dégradés étape par étape pour identifier le problème
    """
    print("🔍 Test de débogage des dégradés\n")
    
    # Test 1: Validation de couleurs
    print("Test 1: Validation de couleurs")
    test_couleurs = [
        "red,blue",
        "red, blue", 
        "#FF0000,#0000FF",
        "#FF0000, #0000FF",
        "red,orange,yellow"  # Plus de 2 couleurs
    ]
    
    for couleur in test_couleurs:
        resultat = valider_couleur(couleur)
        print(f"  '{couleur}' → {resultat} (type: {type(resultat)})")
    
    print()
    
    # Test 2: Création directe de dégradé
    print("Test 2: Création directe de dégradé")
    try:
        creer_degraded_qr("Test dégradé direct", "test_degrade_direct.png", "red", "blue", "white")
        print("  ✅ Dégradé direct créé avec succès!")
    except Exception as e:
        print(f"  ❌ Erreur dégradé direct: {e}")
    
    print()
    
    # Test 3: Test avec couleurs validées
    print("Test 3: Test avec couleurs validées")
    couleurs_validees = valider_couleur("red,blue")
    print(f"  Couleurs validées: {couleurs_validees}")
    
    if isinstance(couleurs_validees, list) and len(couleurs_validees) >= 2:
        try:
            creer_degraded_qr("Test validé", "test_degrade_valide.png", 
                            couleurs_validees[0], couleurs_validees[1], "white")
            print("  ✅ Dégradé avec validation créé avec succès!")
        except Exception as e:
            print(f"  ❌ Erreur dégradé validé: {e}")
    else:
        print("  ❌ Couleurs non validées comme liste")
    
    print()
    
    # Test 4: Reproduction du problème utilisateur
    print("Test 4: Simulation complète")
    print("Simulation de l'entrée utilisateur...")
    
    # Simuler l'entrée: red,blue
    couleur_utilisateur = "red,blue"
    couleur_validee = valider_couleur(couleur_utilisateur)
    
    print(f"  Entrée utilisateur: '{couleur_utilisateur}'")
    print(f"  Résultat validation: {couleur_validee}")
    print(f"  Type: {type(couleur_validee)}")
    print(f"  Est une liste? {isinstance(couleur_validee, list)}")
    
    if isinstance(couleur_validee, list):
        print(f"  Nombre de couleurs: {len(couleur_validee)}")
        print(f"  Couleur 1: {couleur_validee[0]}")
        print(f"  Couleur 2: {couleur_validee[1] if len(couleur_validee) > 1 else 'N/A'}")
        
        try:
            creer_degraded_qr("Test simulation complète", "test_simulation.png", 
                            couleur_validee[0], couleur_validee[1], "white")
            print("  ✅ Simulation complète réussie!")
        except Exception as e:
            print(f"  ❌ Erreur simulation: {e}")
    
    print("\n🎯 Tests terminés!")

if __name__ == "__main__":
    tester_degrades()
