import json
import random


def generate_code():
    code = [random.randint(1, 50) for _ in range(3)]
    return ".".join(str(i) for i in code)


directions = {}
for direction in ["Техническая физика", "Ядерная энергетика и теплофизика",
                  "Биотехнология", "Оптотехника", "Автоматизация технологических процессов",
                  "Бизнес-информатика", "Инноватика", "Информатика и вычислительная техника"]:
    directions[generate_code()] = direction

with open("generated/directions.json", "w") as outfile:
    json.dump(directions, outfile)
