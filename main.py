import csv
import re

all_lines = []
file_name = input()

with open(file_name, encoding='utf-8-sig') as f:
    file_reader = csv.reader(f)
    for i in file_reader:
        all_lines.append(i)
name_row = all_lines.pop(0)

vacancies_all = []
for line in all_lines:
    if len(line) == len(name_row) and '' not in line:
        vacancies_all.append(line)

dic_naming = {'name': 'Название',
              'description': 'Описание',
              'key_skills': 'Навыки',
              'experience_id': 'Опыт работы',
              'premium': 'Премиум-вакансия',
              'employer_name': 'Компания',
              'salary_from': 'Нижняя граница вилки оклада',
              'salary_to': 'Верхняя граница вилки оклада',
              'salary_gross': 'Оклад указан до вычета налогов',
              'salary_currency': 'Идентификатор валюты оклада',
              'area_name': 'Название региона',
              'published_at': 'Дата и время публикации вакансии'}

vacancies = []
for line in vacancies_all:
    dict_vac = {}
    for i in range(len(name_row)):
        values = []
        if line[i].find('\n') != -1:
            for j in line[i].split("\n"):
                values.append(" ".join(re.sub(r"<[^>]+>", "", j).split()))
        else:
            values = " ".join(re.sub(r"<[^>]+>", "", line[i]).split())
        dict_vac[name_row[i]] = values
    vacancies.append(dict_vac)

for i in range(len(vacancies)):
    for key, value in vacancies[i].items():
        if type(value).__name__ == "list":
            print(f"{dic_naming[key]}: {', '.join(value)}")
        else:
            if value == "FALSE" or value == "false" or value == 'False':
                value = "Нет"
            if value == "TRUE" or value == "true" or value == 'True':
                value = "Да"

            print(f"{dic_naming[key]}: {value}")
    print()
