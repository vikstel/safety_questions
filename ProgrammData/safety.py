import docx
import json
import os


def get_json_questions(path_to_files):
    catalog = os.listdir(path)
    docx_files = []
    count = 0
    counts = []
    questions = []
    answers = []
    for file in catalog:
        if 'docx' in file:
            docx_files.append(file)
    for document in docx_files:
        doc = docx.Document(document)
        # получаем первую таблицу в документе
        table = doc.tables[0]
        # читаем данные из таблицы
        for row in table.rows:
            for cell in row.cells[1:2]:
                count += 1
                counts.append(count)
                questions.append(cell.text)
            for cell in row.cells[2:]:
                c_text = cell.text
                c_text = c_text.replace('\n', ' ').replace('\t', ' ')
                answers.append(c_text)

    abvr_dict = dict(zip(questions, answers))
    with open('questions.json', 'a', encoding='utf-8') as file:
        json.dump(abvr_dict, file, indent=4, ensure_ascii=False)
    # with open('questions.json', 'r', encoding='utf-8') as file:
    #     data = json.load(file)
    # return data


if __name__ == '__main__':
    path = 'C:\\Users\\v.shumov\\PycharmProjects\\safety_questions\\ProgrammData'
    quest = get_json_questions(path)
    # print(quest)



