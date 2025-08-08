#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Démonstration rapide du générateur de QR codes Fleur-Accacia
"""

from qrCode import *

def demo_rapide():
    """
    Démonstration rapide de toutes les fonctionnalités
    """
    print("🚀 DÉMONSTRATION RAPIDE - Générateur QR Fleur-Accacia\n")
    
    # Exemple 1: QR simple
    print("1️⃣ QR Code simple...")
    generer_qr_code("https://github.com/FleurAccacia", "demo_simple.png")
    
    # Exemple 2: QR coloré
    print("\n2️⃣ QR Code coloré...")
    generer_qr_code_personnalise(
        "QR Code coloré par Fleur-Accacia", 
        "demo_colore.png", 
        "darkblue", 
        "lightyellow"
    )
    
    # Exemple 3: QR avec logo
    print("\n3️⃣ QR Code avec logo...")
    logo = creer_logo_simple("demo_logo.png", "red", 80)
    generer_qr_code_avec_logo(
        "QR Premium Fleur-Accacia",
        "demo_avec_logo.png",
        logo,
        "purple",
        "lightcyan",
        0.25
    )
    
    print("\n✅ Démonstration terminée !")
    print("💙 Merci d'avoir testé le générateur QR de Fleur-Accacia !")

if __name__ == "__main__":
    demo_rapide()
