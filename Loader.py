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


if __name__ == "__main__":
    conn = psycopg2.connect(database="timetable", user="postgres", password="kyrlik", host="localhost", port="5433")
    load_room(conn)
    conn.commit()
    conn.close()
