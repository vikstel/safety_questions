import docx


doc = docx.Document('abvr.docx')

# получаем первую таблицу в документе
table = doc.tables[0]

# читаем данные из таблицы
count = 0
counts = []
questions = []
answers = []
for row in table.rows:
    for cell in row.cells[1:2]:
        count += 1
        counts.append(count)
        questions.append(cell.text)
    for cell in row.cells[2:]:
        c_text = cell.text
        c_text = c_text.replace('\n', '').replace('\t', '')
        answers.append(c_text)

print(answers)



