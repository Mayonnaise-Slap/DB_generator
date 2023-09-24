import json
import random

if __name__ == "__main__":
    with open(f"generated/campus.json") as inp:
        campus = json.load(inp)

    rooms = {}
    for campus_id in campus:
        for floor in range(1, 5):
            for rooms_on_floor in range(1, random.randint(1, 5) * 5):
                room = f"{random.randint(1, 4)}{floor}{str(rooms_on_floor).rjust(2, '0')}"
                rooms[room] = {"campus": campus_id,
                               "space": random.randint(3, 12) * 5}
    with open(f"generated/rooms.json", "w") as out:
        json.dump(rooms, out)
