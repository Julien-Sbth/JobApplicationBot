# 🤖 Auto-CV Sender

Ce projet utilise **Selenium** pour automatiser l'envoi de candidatures à des offres d'alternance ou de stage.

## 🚀 Objectif

Automatiser l'envoi de CV à travers différentes plateformes de recrutement, tout en adaptant le processus selon l'entreprise ciblée.

## 🛠️ Fonctionnalités

- Automatisation du remplissage de formulaires de candidature
- Envoi de CV via les plateformes **LinkedIn** et **Indeed**
- Détection intelligente de l'entreprise pour adapter la procédure
- Support natif pour les entreprises suivantes :
  - **Airbus**
  - **Orange**
  - **Sopra Steria**
  - **BPCE**

## 🧠 Technologies utilisées

- [Selenium](https://www.selenium.dev/) pour l'automatisation du navigateur
- Python 3
- WebDriver Chrome ou Firefox

## 📁 Structure

```bash
.
## 📁 Structure du projet

```bash
.
├── Core/
│   ├── __init__.py
│   ├── browser_setup.py
│   ├── company_detection.py
│   ├── config.py
│   ├── linkedin_app.py
│   └── linkedin_login.py
├── Data/
│   ├── CV/
│   │   └── Recherche Alternance Cybersécurité.pdf
│   └── Screenshots/
├── Modules/
│   ├── cv_upload.py
│   └── popup_handler.py
├── job_application.py
├── README.md
└── .gitignore

