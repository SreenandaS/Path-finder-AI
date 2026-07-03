import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Initialize model
model = genai.GenerativeModel("gemini-2.5-flash")


def create_plan(profile, ranked_opportunities):
    prompt = f"""
You are an expert AI Career Planning Agent.

Student Profile:
{profile}

Recommended Opportunities:
{ranked_opportunities}

Create a personalized 4-week action plan.

Include:

- Skills to improve
- Documents to prepare
- Application deadlines
- Interview preparation
- Weekly goals

Return only plain text.
"""

    response = model.generate_content(prompt)

    return response.text


if __name__ == "__main__":

    profile = {
        "skills": ["Python", "React"],
        "career_interest": "Software Engineering"
    }

    ranked_opportunities = [
        {
            "title": "Google STEP Internship",
            "missing_skills": ["Data Structures"],
            "priority": "High"
        },
        {
            "title": "IEEE AI Hackathon",
            "missing_skills": ["Machine Learning"],
            "priority": "Medium"
        }
    ]

    result = create_plan(profile, ranked_opportunities)

    print(result)