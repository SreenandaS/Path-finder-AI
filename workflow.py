from profile_agent import create_profile
from collector import load_opportunities
from filter_agent import filter_opportunities
from ranking_agent import rank_opportunities
from planner_agent import create_plan


def run_workflow(resume_text, student_data):

    print("\n========== PROFILE AGENT ==========\n")

    profile = create_profile(
        resume_text,
        student_data
    )

    print(profile)

    print("\n========== OPPORTUNITY COLLECTOR ==========\n")

    opportunities = load_opportunities()

    print(f"Loaded {len(opportunities)} opportunities.")

    print("\n========== FILTER AGENT ==========\n")

    filtered = filter_opportunities(
        profile,
        opportunities
    )

    print(f"Filtered {len(filtered)} opportunities.\n")

    print("\n========== RANKING AGENT ==========\n")

    ranked = rank_opportunities(
        profile,
        filtered
    )

    print(ranked)

    print("\n========== PLANNING AGENT ==========\n")

    plan = create_plan(
        profile,
        ranked
    )

    print(plan)

    return {
        "profile": profile,
        "filtered_opportunities": filtered,
        "ranked_opportunities": ranked,
        "career_plan": plan
    }


if __name__ == "__main__":

    resume_text = """
    Prarthana Mohan

    B.Tech Computer Science and Engineering

    Skills:
    Python
    React
    Machine Learning
    SQL

    Projects:
    PathFinder AI

    Interested in Software Engineering
    """

    student_data = {
        "age": 19,
        "annual_income": 200000,
        "category": "General",
        "state": "Kerala",
        "career_interest": "Software Engineering"
    }

    result = run_workflow(
        resume_text,
        student_data
    )

    print("\n========== FINAL OUTPUT ==========\n")

    print(result)