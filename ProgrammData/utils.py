import json
import random
import sqlite3


# with open('questions.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)
#
# question_list = []
# for k, v in data.items():
#     question_list.append([k,v])
#
#
# with sqlite3.connect('questions.db') as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS question (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     question TEXT,
#     answer TEXT
#     )
#     """)
#     cur.executemany("""
#     INSERT INTO question VALUES (NULL, :question, :answer)""", question_list)

random_number = random.choices([i for i in range(1,89)], k=10)
print(random_number)
for num in random_number:
    with sqlite3.connect('../questions.db') as con:
        cur = con.cursor()
        cur.execute("""SELECT question, answer FROM question WHERE id = (?)""", (num, ))
        text = cur.fetchall()
        print(text[0][0])
        print('=====================')
        print(text[0][1])




