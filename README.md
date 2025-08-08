# Générateur de Code QR Python 📱

Un script Python simple et efficace pour générer des codes QR personnalisables.

## 📋 Fonctionnalités

- ✅ Génération de codes QR basiques
- 🎨 Codes QR avec couleurs personnalisées
- 📍 Support des coordonnées géographiques
- 🔗 Support des URLs
- 💬 Mode interactif
- 📁 Sauvegarde automatique des images

## 🚀 Installation

1. Clonez ce dépôt :
```bash
git clone https://github.com/VOTRE_USERNAME/qr-code-generator.git
cd qr-code-generator
```

2. Installez les dépendances :
```bash
pip install qrcode[pil]
```

## 📖 Utilisation

### Exécution du script complet avec exemples :
```bash
python qrCode.py
```

### Utilisation des fonctions dans votre code :

#### Code QR simple :
```python
from qrCode import generer_qr_code

# Générer un QR code avec du texte
generer_qr_code("Votre texte ici", "mon_qr.png")

# Générer un QR code avec une URL
generer_qr_code("https://www.example.com", "qr_url.png")
```

#### Code QR personnalisé :
```python
from qrCode import generer_qr_code_personnalise

# QR code avec des couleurs personnalisées
generer_qr_code_personnalise(
    "Mon texte coloré",
    "qr_colore.png",
    couleur_remplissage="blue",
    couleur_fond="yellow"
)
```

## 📝 Exemples inclus

Le script génère automatiquement plusieurs exemples :

1. **qr_texte.png** - Code QR avec du texte simple
2. **qr_url.png** - Code QR avec une URL GitHub
3. **qr_coordonnees.png** - Code QR avec les coordonnées de Paris
4. **qr_colore.png** - Code QR coloré (bleu foncé sur fond gris)
5. **Mode interactif** - Saisissez vos propres données

## 🛠️ Paramètres configurables

### `generer_qr_code()`
- `donnees` (str) : Les données à encoder
- `nom_fichier` (str) : Nom du fichier de sortie (défaut: "qr_code.png")
- `taille` (int) : Taille des cases du QR code (défaut: 10)
- `bordure` (int) : Taille de la bordure (défaut: 4)

### `generer_qr_code_personnalise()`
- `donnees` (str) : Les données à encoder
- `nom_fichier` (str) : Nom du fichier de sortie
- `couleur_remplissage` (str) : Couleur des cases du QR code
- `couleur_fond` (str) : Couleur de fond

## 📦 Dépendances

- `qrcode[pil]` - Génération de codes QR avec support d'images PIL
- `Pillow` - Traitement d'images (inclus avec qrcode[pil])

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :

1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commiter vos changements
4. Pusher vers la branche
5. Ouvrir une Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 📧 Contact

- GitHub: [@VOTRE_USERNAME](https://github.com/VOTRE_USERNAME)

---

⭐ N'oubliez pas de mettre une étoile si ce projet vous a été utile !
