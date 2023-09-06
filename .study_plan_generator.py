import json
import random


if __name__ == "__main__":
    with open("directions.txt") as inp:
        directions = json.load(inp)

    study_plans = {}

    for direction in directions:
        for form in ("Очное", "Заочное"):
            cod_op = random.randint(100000, 999999)
            name = directions[direction]
            study_plans[cod_op] = {"name": name, "direction_code": direction,
                                   "stydy_form": form}

    with open("study_plan.txt", "w") as outfile:
        json.dump(study_plans, outfile)