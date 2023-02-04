fighter_scores = {
    "Frodo": 63,
    "Sam": 72,
    "Gandalf": 100,
    "Aragorn": 89,
    "Legolas": 91,
    "Gimli": 83,
}

fighter_grades = {}


def score_to_grade(score):
    if score >= 91:
        return "Legendary"
    elif score >= 81:
        return "Outstanding"
    elif score >= 71:
        return "Acceptable"
    else:
        return "Weak"


for key in fighter_scores:
    fighter_grades[key] = score_to_grade(fighter_scores[key])

print(fighter_grades)
