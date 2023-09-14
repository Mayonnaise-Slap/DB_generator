import json
import random


if __name__ == "__main__":
    with open(".materials/disciplines.txt") as input_file:
        names = [i.strip("\n") for i in input_file.readlines()]
    disciplines = {}
    for name in names:
        discipline_id = random.randint(10000, 99999)
        hours = random.randint(4, 32) * 3
        disciplines[discipline_id] = {"name": name, "hours": hours,
                                      "link": None}
    with open("disciplines.json", "w") as outfile:
        json.dump(disciplines, outfile)
