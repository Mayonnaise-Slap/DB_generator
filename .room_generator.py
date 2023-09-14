import json
import random


if __name__ == "__main__":
    with open(f"generated/campus.json") as inp:
        campus = json.load(inp)

    rooms = {}
    for id in campus:
        for floor in range(1, 5):
            for id in range(1, random.randint(1, 5) * 5):
                room = f"{random.randint(1, 4)}{floor}{str(id).rjust(2, '0')}"
                rooms[room] = {"campus": campus,
                               "space": random.randint(3, 12)*5}
    with open(f"generated/rooms.json", "w") as out:
        json.dump(rooms, out)
