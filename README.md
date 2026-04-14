# Build_Talio
# 🧠 Talent Matching System

Un système simple de matching entre **talents** et **entreprises** basé sur un algorithme de scoring (skills, expérience, localisation, rôle).

---

## 🚀 Objectif

Ce projet a pour but de :

- Calculer un score de compatibilité entre un talent et une entreprise
- Classer les talents du plus pertinent au moins pertinent
- Simuler un système de recrutement simple (type ATS)

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
- Sinon pénalité proportionnelle

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
-
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