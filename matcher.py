class Matcher:
    def __init__(self):
        pass

    def match(self, talent, company):
        score = 0

        # 1. Skills matching (fort poids)
        common_skills = set(talent["skills"]) & set(company["skills"])
        score += len(common_skills) * 3

        # 2. Experience
        diff = talent["experience"] - company["experience"]
        if diff >= 0:
            score += 10
        else:
            score += diff * 2  # pénalité

        # 3. Location
        if talent["location"] == company["location"]:
            score += 5

        # 4. Role match
        if talent["role"] == company["role"]:
            score += 5

        return score

    def rank(self, company, talents):
        results = []

        for t in talents:
            results.append({
                "talent": t["name"],
                "score": self.match(t, company),
                "skills_match": list(set(t["skills"]) & set(company["skills"]))
            })

        return sorted(results, key=lambda x: x["score"], reverse=True)