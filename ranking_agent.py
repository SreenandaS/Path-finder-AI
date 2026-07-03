import json
from collector import load_opportunities
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Initialize Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")


def rank_opportunities(profile, opportunities):
    prompt = f"""
You are an expert AI Career Recommendation Agent.

Student Profile:
{profile}

Available Opportunities:
{opportunities}

Your task:

1. Analyze the student's profile.
2. Check eligibility for each opportunity.
3. Consider:
   - Skills
   - Education
   - Career Interest
   - Age
   - State
   - Category
   - Annual Income
4. Rank the opportunities from best to worst.

Return ONLY valid JSON.

Format:

[
  {{
    "title": "",
    "type": "",
    "score": 0,
    "reason": "",
    "eligibility_status": "",
    "missing_skills": [],
    "priority": ""
  }}
]
"""

    response = model.generate_content(prompt)

    try:
        ranked = json.loads(response.text)
        return ranked

    except Exception as e:
        print("JSON Parsing Error:", e)
        print("Gemini Output:")
        print(response.text)
        return []


if __name__ == "__main__":

    profile = {
        "skills": ["Python", "React"],
        "cgpa": "8.5",
        "interests": ["AI", "Research"]
    }

    opportunities = load_opportunities()
    result = rank_opportunities(
        profile,
        opportunities
    )

    print(result)