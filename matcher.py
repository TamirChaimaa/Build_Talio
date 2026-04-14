class Matcher:
    def __init__(self):
        pass

    # Function that calculates a compatibility score between a talent and a company
    def match(self, talent, company):

        score = 0  # Initialize score

        # 1. Skills matching (high weight)
        # Find common skills between talent and company
        common_skills = set(talent["skills"]) & set(company["skills"])

        # Add 3 points for each common skill
        score += len(common_skills) * 3

        # 2. Experience
        # Calculate experience difference between talent and company requirement
        diff = talent["experience"] - company["experience"]

        if diff >= 0:
            # If talent has equal or more experience → bonus
            score += 10

        # 3. Location
        # Check if talent is in the same location as the company
        if talent["location"] == company["location"]:
            score += 5  # Bonus for same city

        # 4. Role match
        # Check if job role matches (e.g. backend, frontend, etc.)
        if talent["role"] == company["role"]:
            score += 5  # Bonus for same role

        # Return final computed score
        return score

    # Function that ranks talents for a given company
    def rank(self, company, talents):

        results = []  # List that will store ranked results

        for t in talents:
            # Compute score for each talent
            results.append({
                "talent": t["name"],  # Talent name
                "score": self.match(t, company),  # Compatibility score
                "skills_match": list(set(t["skills"]) & set(company["skills"]))  
                # Common skills (used to explain the match)
            })

        # Sort results by score in descending order (best first)
        return sorted(results, key=lambda x: x["score"], reverse=True)