import docx
import json
import os
import sqlite3
import random


def get_json_questions():
    count = 0
    counts = []
    questions = []
    answers = []
    doc = docx.Document('morning_questions.docx')
            # получаем первую таблицу в документе
    table = doc.tables[0]
    # читаем данные из таблицы
    for row in table.rows:
        for cell in row.cells[0:1]:
            count += 1
            counts.append(count)
            questions.append(cell.text)
        for cell in row.cells[1:]:
            c_text = cell.text
            c_text = c_text.replace('\n', ' ').replace('\t', ' ')
            answers.append(c_text)

    morning_questions_dict = dict(zip(questions, answers))
    morning_questions_list = []
    for k, v in morning_questions_dict.items():
        morning_questions_list.append([k, v])

    print(morning_questions_list)
    with sqlite3.connect('morning_questions.db') as con:
        cur = con.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT,
        answer TEXT
        )
        """)
        cur.executemany("""
        INSERT INTO questions VALUES (NULL, :question, :answer)""", morning_questions_list)

    # random_number = random.choices([i for i in range(1, 89)], k=10)
    # print(random_number)
    # for num in random_number:
    #     with sqlite3.connect('../questions.db') as con:
    #         cur = con.cursor()
    #         cur.execute("""SELECT question, answer FROM question WHERE id = (?)""", (num,))
    #         text = cur.fetchall()
    #         print(text[0][0])
    #         print('=====================')
    #         print(text[0][1])



if __name__ == '__main__':
    quest = get_json_questions()
    print(quest)