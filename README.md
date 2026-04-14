# Build_Talio
# 🧠 Talent Matching System

Un système simple de matching entre **talents** et **entreprises** basé sur un algorithme de scoring (skills, expérience, localisation, rôle).

---

## 🚀 Objectif

Ce projet a pour but de :

- Calculer un score de compatibilité entre un talent et une entreprise
- Classer les talents du plus pertinent au moins pertinent

👉 L’objectif principal est de **ship vite une solution fonctionnelle et lisible**

---

## 📁 Structure du projet
Build_Talio
│
├── data.py # Données (talents + entreprises)
├── matcher.py # Logique de scoring & ranking
├── main.py # Point d’entrée du programme
└── README.md


---

## ⚙️ Logique de scoring

Le score est calculé selon plusieurs critères :

### 🧩 Skills
- +3 points par skill commun entre talent et entreprise

### 🎯 Expérience
- +10 points si le talent a une expérience ≥ requise

### 📍 Localisation
- +5 points si même ville

### 👨‍💼 Rôle
- +5 points si le rôle correspond

---

## ▶️ Installation & exécution

### 1. Cloner le projet

```bash
git clone <repo-url>

cd Build_Talio

2. Lancer le programme

python main.py

OR

python3 main.py


🧪 Exemple de sortie
🏢 Company: TechCorp
========================================

👤 Alice Benali
   ⭐ Score: 23
   🔧 Skills match: ['python', 'django', 'api']
----------------------------------------

👤 Sara Zahra
   ⭐ Score: 18
   🔧 Skills match: ['api']
----------------------------------------

👤 Yassine El Amrani
   ⭐ Score: 5
   🔧 Skills match: []
----------------------------------------


📊 Exemple de données
👨‍💻 Talent
{
  "name": "Alice",
  "skills": ["python", "django", "api"],
  "experience": 3,
  "location": "Casablanca",
  "role": "backend"
}
🏢 Company
{
  "name": "TechCorp",
  "skills": ["python", "api", "docker"],
  "experience": 3,
  "location": "Casablanca",
  "role": "backend"
}

📌 Changer l’entreprise utilisée

Dans ce projet, vous pouvez facilement changer l’entreprise utilisée pour effectuer le matching.

Par défaut, la première entreprise de la liste est sélectionnée :

company = companies[0]
🔄 Modifier l’entreprise

Pour tester le système avec une autre entreprise, il suffit de changer l’indice :

company = companies[1]  # deuxième entreprise

ou

company = companies[2]  # troisième entreprise
💡 Remarque

Chaque entreprise contient des critères différents (compétences, rôle, expérience, localisation).

💡 Améliorations possibles
🔥 API REST avec FastAPI ou Express.js
🤖 Matching basé sur IA (embeddings)
📊 Dashboard React pour visualisation
⚖️ Système de poids configurable (JSON config)
🔎 Matching sémantique des 

🛠️ Technologies utilisées
Python 3
Algorithmique simple de scoring
Structures de données (listes, dictionnaires)