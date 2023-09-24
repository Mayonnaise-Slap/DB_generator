import psycopg2
import json


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


if __name__ == "__main__":
    conn = psycopg2.connect(database="timetable", user="postgres", password="kyrlik", host="localhost", port="5433")
    load_connection(conn)
    conn.commit()
    conn.close()
