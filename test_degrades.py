#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test rapide des dégradés de couleurs
"""

from qrCode import creer_degraded_qr, generer_qr_code_avec_logo_et_degrade, creer_logo_simple

def test_degrades():
    """
    Test rapide des dégradés
    """
    print("🌈 TEST DES DÉGRADÉS - Fleur-Accacia\n")
    
    # Test 1: Dégradé rouge vers bleu
    print("1️⃣ Dégradé rouge → bleu...")
    creer_degraded_qr("Test dégradé rouge-bleu", "test_degrade_rouge_bleu.png", "red", "blue")
    
    # Test 2: Dégradé doré vers violet
    print("\n2️⃣ Dégradé doré → violet...")
    creer_degraded_qr("Test dégradé doré-violet", "test_degrade_dore_violet.png", "#FFD700", "purple")
    
    # Test 3: Dégradé avec logo
    print("\n3️⃣ Dégradé vert → orange avec logo...")
    logo = creer_logo_simple("logo_test_degrade.png", "white", 80)
    generer_qr_code_avec_logo_et_degrade(
        "Dégradé avec logo - Fleur-Accacia", 
        "test_degrade_avec_logo.png",
        logo,
        "green",
        "orange",
        "white",
        0.25
    )
    
    print("\n✅ Tests de dégradés terminés !")
    print("🎨 Fichiers créés :")
    print("   - test_degrade_rouge_bleu.png")
    print("   - test_degrade_dore_violet.png") 
    print("   - test_degrade_avec_logo.png")
    print("\n💙 Merci d'avoir testé les dégradés de Fleur-Accacia !")

if __name__ == "__main__":
    test_degrades()
