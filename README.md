#  Générateur de Code QR - Fleur-Accacia

> **Un générateur de codes QR gratuit, personnalisable et sans limites !**

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-FleurAccacia-black.svg)](https://github.com/FleurAccacia)

## 🌟 Pourquoi ce projet ?

**Le problème :** Les générateurs de codes QR en ligne sont souvent :
- 💰 **Payants** pour les fonctionnalités avancées
- 🔒 **Limités** en personnalisation
- 📊 **Collecteurs de données** de vos liens/informations
- ⏰ **Temporaires** - vos QR codes peuvent disparaître

**Notre solution :** Un générateur **100% gratuit**, **local** et **personnalisable** qui vous appartient !

## ✨ Fonctionnalités

### 🎯 **Niveau 1 : QR Code Basique**
- ✅ Génération simple et rapide
- ✅ QR codes noir et blanc classiques
- ✅ Support de tous types de contenus (URL, texte, coordonnées GPS, etc.)
- ✅ Sauvegarde locale en haute qualité

### 🎨 **Niveau 2 : Personnalisation Standard**
- ✅ **Couleurs personnalisées** pour le QR code et l'arrière-plan
- ✅ **8 couleurs prédéfinies** + couleurs personnalisées (hex, noms)
- ✅ **Noms de fichiers** personnalisés
- ✅ **Validation automatique** des couleurs

### 🌈 **Niveau 3 : Personnalisation Avancée**
- ✅ **Dégradés de couleurs** (combinaison de 2 couleurs)
- ✅ **Logos personnalisés** au centre du QR code
- ✅ **Logos automatiques** (création de logos simples)
- ✅ **Masques ronds** pour les logos
- ✅ **Correction d'erreur élevée** pour maintenir la lisibilité

### 🖥️ **Niveau 4 : Interface Graphique** *(À venir)*
- 🔄 Interface utilisateur visuelle
- 🔄 Aperçu en temps réel
- 🔄 Drag & drop pour les logos
- 🔄 Sélecteur de couleurs graphique

## 🚀 Installation

### Prérequis
- Python 3.7 ou plus récent
- pip (gestionnaire de packages Python)

### Installation rapide
```bash
# 1. Clonez le dépôt
git clone https://github.com/FleurAccacia/Generator-qrcode.git
cd Generator-qrcode

# 2. Installez les dépendances
pip install qrcode[pil]

# 3. Lancez le générateur
python qrCode.py
```

## 📖 Utilisation

### 🎮 Mode Interactif
Lancez simplement le script et suivez les instructions :
```bash
python qrCode.py
```

L'interface vous guidera à travers :
1. **Contenu** : Entrez votre URL, texte, ou données
2. **Type** : Choisissez simple ou avec couleurs
3. **Couleurs** : Sélectionnez parmi nos propositions ou entrez vos propres couleurs
4. **Logo** : Ajoutez votre logo ou créez-en un simple
5. **Résultat** : Votre QR code est généré et sauvegardé !

### 💻 Utilisation Programmatique

#### QR Code simple
```python
from qrCode import generer_qr_code

# QR code basique
generer_qr_code("https://github.com/FleurAccacia", "mon_qr.png")
```

#### QR Code coloré
```python
from qrCode import generer_qr_code_personnalise

# QR code avec couleurs
generer_qr_code_personnalise(
    "Mon site web", 
    "qr_colore.png", 
    "darkblue", 
    "lightyellow"
)
```

#### QR Code avec dégradé
```python
from qrCode import creer_degraded_qr

# QR code avec dégradé
creer_degraded_qr(
    "QR Premium", 
    "qr_degrade.png", 
    "red", 
    "orange", 
    "white"
)
```

#### QR Code avec logo
```python
from qrCode import generer_qr_code_avec_logo, creer_logo_simple

# Créer un logo simple
logo = creer_logo_simple("logo.png", "blue", 80)

# QR code avec logo
generer_qr_code_avec_logo(
    "QR avec logo",
    "qr_logo.png",
    logo,
    "purple",
    "lightcyan",
    0.25
)
```

## 🎨 Exemples de Couleurs

### Couleurs Prédéfinies
| Nom | Couleur | Code |
|-----|---------|------|
| Noir | ⚫ | `black` |
| Bleu foncé | 🔵 | `darkblue` |
| Vert foncé | 🟢 | `darkgreen` |
| Rouge | 🔴 | `red` |
| Violet | 🟣 | `purple` |
| Orange foncé | 🟠 | `darkorange` |
| Marron | 🤎 | `brown` |

### Couleurs Personnalisées
```
Formats acceptés :
- Noms : blue, red, green, yellow...
- Hex : #FF0000, #00FF00, #0000FF...
- RGB : rgb(255, 0, 0)
```

### Dégradés
```
Entrez deux couleurs séparées par une virgule :
- "red, orange" → Dégradé rouge vers orange
- "#FF0000, #FFFF00" → Dégradé rouge vers jaune
- "blue, lightblue" → Dégradé bleu vers bleu clair
```

## 📁 Structure du Projet

```
Generator-qrcode/
├── 📄 qrCode.py              # Script principal
├── 📄 demo_qr.py             # Script de démonstration
├── 📄 test_degrades.py       # Tests des dégradés
├── 📄 README.md              # Documentation
├── 🖼️ Exemples générés/
│   ├── qr_simple.png
│   ├── qr_colore.png
│   ├── qr_degrade.png
│   └── qr_avec_logo.png
└── 🎨 Logos créés/
    ├── logo_simple.png
    └── logo_utilisateur.png
```

## 🛠️ Dépendances

```txt
qrcode[pil] >= 7.4.2    # Génération de QR codes
Pillow >= 9.0.0         # Traitement d'images
```

## 🎯 Feuille de Route

- [x] **Phase 1** : QR codes basiques ✅
- [x] **Phase 2** : Personnalisation couleurs ✅
- [x] **Phase 3** : Dégradés et logos ✅
- [ ] **Phase 4** : Interface graphique 🔄
- [ ] **Phase 5** : Export batch multiple
- [ ] **Phase 6** : Templates prédéfinis
- [ ] **Phase 7** : API REST

## 🤝 Contribution

Les contributions sont les bienvenues ! 

1. **Fork** le projet
2. **Créez** une branche pour votre fonctionnalité
3. **Committez** vos changements
4. **Poussez** vers la branche
5. **Ouvrez** une Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 👥 Auteur

**Fleur-Accacia** - *Développeuse principale*
- GitHub: [@FleurAccacia](https://github.com/FleurAccacia)
- Email: graciajulienne@gmail.com

## 🙏 Remerciements

- **qrcode** - Bibliothèque Python pour la génération de QR codes
- **Pillow (PIL)** - Traitement d'images en Python
- **Communauté Python** - Pour les outils formidables

## 📝 Changelog

### v1.0.0 (Août 2025)
- ✅ QR codes basiques
- ✅ Personnalisation couleurs
- ✅ Dégradés de couleurs
- ✅ Support des logos
- ✅ Interface utilisateur interactive
- ✅ Validation automatique des couleurs

---

⭐ **N'oubliez pas de mettre une étoile si ce projet vous a été utile !**

💙 **Merci d'utiliser le Générateur QR de Fleur-Accacia !**