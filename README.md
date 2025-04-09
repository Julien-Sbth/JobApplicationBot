# 🤖 Auto-CV Sender

Ce projet utilise **Selenium** pour automatiser l'envoi de candidatures à des offres d'alternance ou de stage, simplifiant ainsi le processus de recherche d'emploi.

## 🚀 Objectif

Automatiser l'envoi de CV à travers différentes plateformes de recrutement, tout en adaptant le processus selon l'entreprise ciblée. Cela permet de gagner du temps et d'augmenter l'efficacité des candidatures.

## 🛠️ Fonctionnalités

- **Automatisation du remplissage de formulaires de candidature** : Remplit automatiquement les champs requis pour postuler à une offre.
- **Envoi de CV via les plateformes** : Supporte actuellement **LinkedIn** et **Indeed**.
- **Détection intelligente de l'entreprise** : Adapte la procédure de candidature en fonction de l'entreprise ciblée.
- **Support natif pour les entreprises suivantes** :
  - **Airbus**
  - **Orange**
  - **Sopra Steria**
  - **BPCE**

## 🧠 Technologies utilisées

- [Selenium](https://www.selenium.dev/) : Pour l'automatisation du navigateur.
- **Python 3** : Langage de programmation principal.
- **WebDriver Chrome ou Firefox** : Pour interagir avec le navigateur.

## 📁 Structure du projet

```bash
.
├── Core/
│   ├── __init__.py
│   ├── browser_setup.py        # Configuration du navigateur
│   ├── company_detection.py    # Détection de l'entreprise cible
│   ├── config.py               # Configuration générale
│   ├── linkedin_app.py         # Gestion des applications LinkedIn
│   └── linkedin_login.py       # Connexion à LinkedIn
├── Data/
│   ├── CV/
│   │   └── Recherche Alternance Cybersécurité.pdf  # Exemple de CV
│   └── Screenshots/            # Captures d'écran des processus
├── Modules/
│   ├── cv_upload.py            # Module de téléchargement de CV
│   └── popup_handler.py        # Gestion des pop-ups
├── job_application.py          # Script principal d'application
├── README.md                   # Documentation du projet
└── .gitignore                  # Fichiers et dossiers ignorés par Git
```

## 🔑 Configuration

Pour configurer le projet, suivez ces étapes :

1. Créez un fichier `.env` à la racine du projet
2. Ajoutez les variables d'environnement suivantes :

```env
# Identifiants LinkedIn
LINKEDIN_EMAIL="votre_email@exemple.com"
LINKEDIN_PASSWORD="votre_mot_de_passe"

# URL de l'offre d'emploi à postuler
JOB_URL="https://www.linkedin.com/jobs/view/123456789"

# Chemin vers votre CV (format PDF recommandé)
CV_PATH="./documents/mon_cv.pdf"