import json
import random


def generate_isu():
    return random.randint(300000, 399999)


class student:
    def __init__(self):
        self.isu = generate_isu()
        self.name = self.generate_name()
        self.phone = self.generate_phone()
        self.group = self.generate_group()

    @staticmethod
    def generate_name():
        name = ""
        male = bool(random.getrandbits(1))
        if male:
            name += random.choice(list(open('ru-pnames-list/lists/male_names_rus.txt'))).strip("\n") + ' '
            name += random.choice(list(open('ru-pnames-list/lists/male_surnames_rus.txt'))).strip('\n')
        else:
            end = "а"
            name += random.choice(list(open('ru-pnames-list/lists/female_names_rus.txt'))).strip("\n") + ' '
            name += random.choice(list(open('ru-pnames-list/lists/male_surnames_rus.txt'))).strip('\n')
            if name[-1] == "й":
                end = "я"
                name = name[:-1]
            name += end
        return name

    @staticmethod
    def generate_phone():
        phone = str(random.randint(6, 9))
        for i in range(9):
            phone += str(random.randint(0, 9))
        return phone

    @staticmethod
    def generate_group():
        group = random.choice(list(open('.materials/groups.txt'))).strip("\n")
        return group


if __name__ == "__main__":
    number = 200
    students = {}
    for i in range(number):
        loc = student()
        students[loc.isu] = {"name": loc.name, "phone": loc.phone,
                             "group": loc.group}

    with open("students.txt", "w") as outfile:
        json.dump(students, outfile)
