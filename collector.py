import json


def load_opportunities():

    with open("opportunities.json", "r", encoding="utf-8") as file:

        opportunities = json.load(file)

    return opportunities