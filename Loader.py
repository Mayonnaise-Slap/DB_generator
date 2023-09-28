import random

import psycopg2
import json
from config import config
import datetime


def load_campus(conn):
    with open('generated/campus.json') as f:
        data = json.load(f)

    cur = conn.cursor()
    for record in data:
        cur.execute(f"""INSERT INTO "расписание занятий"."адрес" (номер_корпуса, город, название_корпуса, алрес_корпуса) VALUES ({int(record)}, '{data[record]['city']}', '{data[record]['campus_name']}', '{data[record]['campus_adress']}')""")


def load_room(conn):
    with open('generated/rooms.json') as f:
        data = json.load(f)

    cur = conn.cursor()
    for record in data:
        cur.execute(
            f"""INSERT INTO "расписание занятий"."кабинет" (номер_кабинета, номер_корпуса, количество_мест) VALUES ({int(record)}, '{data[record]['campus']}', '{data[record]['space']}')""")


def load_tutor(conn):
    with open("generated/tutors.json") as f:
        data = json.load(f)

    cur = conn.cursor()
    for id in data:
        record = data[id]
        cur.execute(
            f"""INSERT INTO "расписание занятий"."преподаватель" (ИСУ_преподаватель, ФИО, телефон, должность) VALUES ('{id}', '{record["name"]}', '{record["phone"]}', '{record["title"]}')"""
        )


def load_student(conn):
    with open("generated/students.json") as f:
        data = json.load(f)

    cur = conn.cursor()
    for id in data:
        record = data[id]
        cur.execute(
            f"""INSERT INTO "расписание занятий"."студент" (ИСУ_студента, ФИО, телефон, номер_группы) VALUES ('{id}', '{record["name"]}', '{record["phone"]}', '{record["group"]}')"""
        )

def direction(conn):
    with open("generated/study_plan.json") as f:
        data = json.load(f)

    cur = conn.cursor()
    for id in data:
        record = data[id]
        if record["stydy_form"] != "Очное":
            continue
        cur.execute(
            f"""INSERT INTO "расписание занятий"."направление подготовки" (код_направления, название) VALUES ('{record["direction_code"]}', '{record["name"]}')"""
        )


def load_study_plan(conn):
    with open("generated/study_plan.json") as f:
        data = json.load(f)

    cur = conn.cursor()
    for id in data:
        record = data[id]
        cur.execute(
            f"""INSERT INTO "расписание занятий"."ОП" (код_ОП, название, код_направления, форма_обучения) VALUES ('{id}', '{record["name"]}', '{record["direction_code"]}', '{record["stydy_form"]}')"""
        )


def load_discipline(conn):
    with open("generated/disciplines.json") as f:
        data = json.load(f)

    cur = conn.cursor()
    for id in data:
        record = data[id]
        cur.execute(
            f"""INSERT INTO "расписание занятий"."дисциплины" (код_дисциплины, название, количество_часов) VALUES ('{id}', '{record["name"]}', '{record["hours"]}')"""
        )

def load_connection(conn):
    with open("generated/disciplines_in_plan.json") as f:
        data = json.load(f)

    cur = conn.cursor()
    for line in data:
        cur.execute(
            f"""INSERT INTO "расписание занятий"."список дисциплин вУП" (код_направления, код_дисциплины, семестр_изучения) VALUES ('{line["plan_id"]}', '{line["discipline_id"]}', '{line["semester"]}')"""
        )

def load_uch_plan(conn):
    with open("generated/study_plan.json") as f:
        data = json.load(f)
    cur = conn.cursor()
    for code_op in data:
        cur.execute(
            f"""INSERT INTO "расписание занятий"."учебный план" (номер_уп, дата_набора, код_ОП) VALUES ('{random.randint(111111, 999999)}', '{datetime.datetime(random.randint(2018, 2024), 9, 1)}', '{code_op}')"""
        )

def load_in_group(conn):
    with open(f"generated/students.json") as f:
        student_data = json.load(f)
    with open(f".materials/groups.txt") as f:
        groups = [i.strip("\n") for i in f.readlines()]
    cur = conn.cursor()
    for student in student_data:
        year_start = random.randint(2018, 2024)
        cur.execute(
            f"""INSERT INTO "расписание занятий"."состав группы" (номер_группы, ИСУ_студента, дата_начала, дата_окончания) VALUES ('{random.choice(groups)}', '{student}', '{datetime.datetime(year_start, 9, 1)}', '{datetime.datetime(year_start+4, 6, 30)}')"""
        )


def load_study_group(conn):
    with open(f".materials/groups.txt") as f:
        groups = [i.strip("\n") for i in f.readlines()]

    with open("generated/study_plan.json") as f:
        plans = json.load(f)

    cur = conn.cursor()
    for group in groups:
        year_start = random.randint(2018, 2024)
        cur.execute(
            f"""INSERT INTO "расписание занятий"."учебная группа" (номер_группы, дата_формирование, дата_расформирование, код_ОП)
             VALUES ('{group}', '{datetime.datetime(year_start, 9, 1)}', '{datetime.datetime(year_start+4, 6, 30)}', '{random.choice(list(plans))}')"""
        )


def load_timetable(conn):
    times = [[8, 20], [10, 0], [11, 40], [13, 30], [15, 20], [17, 0], [18, 40]]
    types = ["лабораторная", "практика", "лекция"]
    with open(f"generated/rooms.json") as f:
        cabinets = list(json.load(f))
    with open(f".materials/groups.txt") as f:
        groups = [i.strip('\n') for i in f.readlines()]
    with open(f"generated/tutors.json") as f:
        tutor_ids = list(json.load(f))
    with open("generated/disciplines.json") as f:
        discipline_ids = list(json.load(f))
    cur = conn.cursor()

    lesson_index = 1001
    # print(random.choice(groups))
    # print(random.choice(cabinets))
    # print(random.choice(tutor_ids))
    # print(random.choice(discipline_ids))
    # print(random.choice(types))

    for _ in range(10000):
        time = random.choice(times)
        year = random.randint(2021, 2024)
        cur.execute(
            f"""INSERT INTO "расписание занятий"."расписание"
             (lesson_id, номер_группы, номер_кабинет, учебный_год, ИСУ_преподаватель, код_дисциплины, время_начала, время_окончания, дата_проведения, вид_занятия)
            VALUES ('{lesson_index}', '{random.choice(groups)}','{random.choice(cabinets)}','{datetime.date(year, 9, 1)}','{random.choice(tutor_ids)}',
            '{random.choice(discipline_ids)}', '{datetime.time(time[0], time[1])}','{(datetime.datetime(year = 1, month=1, day=1, hour=time[0], minute=time[1]) + datetime.timedelta(minutes=90)).time()}',
            '{datetime.datetime(year, random.randint(1, 12), random.randint(1,28))}', '{random.choice(types)}')"""
        )
        lesson_index += 1


if __name__ == "__main__":
    c = config()
    conn = psycopg2.connect(database=c.database, user=c.user, password=c.password, host=c.host, port=c.port)
    load_timetable(conn)
    conn.commit()
    conn.close()
