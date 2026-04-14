from data import talents, companies
from matcher import Matcher

def run():
    
    matcher = Matcher()

    company = companies[0]  

    print("\n🏢 Company:", company["name"])
    print("=" * 40)

    ranked = matcher.rank(company, talents)

    for r in ranked:
        print(f"👤 {r['talent']}")
        print(f"   ⭐ Score: {r['score']}")
        print(f"   🔧 Skills match: {r['skills_match']}")
        print("-" * 40)


if __name__ == "__main__":
    run()