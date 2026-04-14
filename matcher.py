class Matcher:
    def __init__(self):
        pass
    # Fonction qui calcule un score de compatibilité entre un talent et une entreprise
    def match(self, talent, company):
        
        
        score = 0  # Initialisation du score

        # 1. Skills matching (fort poids)
        # On cherche les compétences communes entre le talent et l'entreprise
        common_skills = set(talent["skills"]) & set(company["skills"])
        
        # On ajoute 3 points pour chaque compétence commune
        score += len(common_skills) * 3

        # 2. Experience
        # Calcul de la différence d'expérience entre le talent et le besoin de l'entreprise
        diff = talent["experience"] - company["experience"]
        
        if diff >= 0:
            # Si le talent a autant ou plus d'expérience → bonus
            score += 10
        # 3. Location
        # Vérifie si le talent est dans la même localisation que l'entreprise
        if talent["location"] == company["location"]:
            score += 5  # Bonus si même ville

        # 4. Role match
        # Vérifie si le rôle correspond (ex: backend, frontend, etc.)
        if talent["role"] == company["role"]:
            score += 5  # Bonus si même rôle

        # Retourne le score final
        return score

    
     # Fonction qui classe les talents pour une entreprise donnée
    def rank(self, company, talents):
        
        results = []  # Liste qui va contenir les résultats

        for t in talents:
            # Pour chaque talent, on calcule son score
            results.append({
                "talent": t["name"],  # Nom du talent
                "score": self.match(t, company),  # Score calculé avec la fonction match
                "skills_match": list(set(t["skills"]) & set(company["skills"]))  
                # Liste des compétences communes (utile pour expliquer le match)
            })

        # On trie les résultats par score décroissant (du meilleur au moins bon)
        return sorted(results, key=lambda x: x["score"], reverse=True)