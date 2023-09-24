import json
import random


with open(r"../generated/disciplines.json") as dis:
    disciplines = json.load(dis)

with open(r"../generated/study_plan.json") as pn:
    plans = json.load(pn)

connection = []

for plan_id in plans:
    plan_code = plans[plan_id]["direction_code"]
    for semester in range(1, 9):
        for subj_count in range(5):
            row = {
                "discipline_id": random.choice(list(disciplines)),
                "plan_id": plan_code,
                "semester": semester
            }
            connection.append(row)

with open(r"../generated/disciplines_in_plan.json", "w") as out:
    json.dump(connection, out)
