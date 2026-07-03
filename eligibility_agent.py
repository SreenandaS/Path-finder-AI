def check_elilgibility(profile,opportunities):
    eligible=[]
    for opportunity in opportunities:
        if profile["annual_income"]<=opportunity["income_limit"]:
            eligible.append(opportunity)
    return eligible