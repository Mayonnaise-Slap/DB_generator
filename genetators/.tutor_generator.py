import json
import random


class tutor:
    def __init__(self):
        self.isu = self.generate_isu()
        self.name = self.generate_name()
        self.phone = self.generate_phone()
        self.title = self.generate_title()

    @staticmethod
    def generate_isu():
        return random.randint(300000, 399999)

    @staticmethod
    def generate_name():
        name = ""
        male = bool(random.getrandbits(1))
        if male:
            name += random.choice(list(open('.materials/male_names_rus.txt'))).strip("\n") + ' '
            name += random.choice(list(open('.materials/male_surnames_rus.txt'))).strip('\n')
        else:
            end = "а"
            name += random.choice(list(open('.materials/female_names_rus.txt'))).strip("\n") + ' '
            name += random.choice(list(open('.materials/male_surnames_rus.txt'))).strip('\n')
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
    def generate_title():
        return random.choices(list(open(".materials/titles.txt")), weights=(47, 47, 6))[0].strip("\n")


if __name__ == "__main__":
    number = 20
    tutors = {}
    for i in range(number):
        loc = tutor()
        tutors[loc.isu] = {"name": loc.name, "phone": loc.phone,
                           "title": loc.title}

    with open("generated/tutors.json", "w") as outfile:
        json.dump(tutors, outfile)
