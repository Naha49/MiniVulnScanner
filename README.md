# 🔍 MiniVulnScanner

Un petit outil Python qui permet de scanner une plage d'adresses IP pour détecter les ports ouverts et les services associés, en utilisant Nmap.  
Ce projet a été réalisé dans un objectif pédagogique en lien avec un apprentissage en cybersécurité.

---

## 🎯 Objectif

- Identifier les services exposés sur un réseau local
- Automatiser un scan réseau avec Python
- Renforcer ses compétences en sécurité, réseau et scripting

---

## 🛠️ Technologies utilisées

- Python 3
- Bibliothèque `python-nmap`
- Nmap (doit être installé sur la machine)

---

## ⚙️ Installation

1. Clonez ou téléchargez le projet :


git clone https://github.com/pseudo/MiniVulnScanner.git
cd MiniVulnScanner


2. Créez un environnement virtuel et installez les dépendances :

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

3. Assurez-vous que Nmap est bien installé :

# Pour Linux
sudo apt install nmap

# Pour macOS
brew install nmap

🚀 Utilisation

Lancer le script :
python scanner.py

Suivez les instructions :

    Entrez la plage IP à scanner : 192.168.1.0/24

    Entrez les ports à scanner : 22,80,443 ou 1-1024
    

👨‍💻 Auteur

Naha49
