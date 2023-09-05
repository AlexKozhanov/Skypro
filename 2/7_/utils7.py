import json
import os.path

def load_students(path):
    '''Возвращает студентов'''

    if not os.path.exists(path):
        return []

    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data

def load_professions(path):
    '''Возвращает студентов'''

    if not os.path.exists(path):
        return []

    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data

def get_student_by_pk(all_students, pk):
    '''Из списка студентов достаёт нужную по её pk'''

    for one_student in all_students:
        if one_student["pk"] == pk:
            return one_student

def get_profession_by_title(all_professions, title):
    '''Из списка профессий достаёт нужную по её названию
    :param all_professions
    :param title
    :return:
    '''
    title = title.title()
    for one_prof in all_professions:
        if one_prof["title"] == title:
            return one_prof

def check_fitness(student, profession):
    '''
    Возвращает соответствие навыков студента навыкам профессии в формате
    {
        "has": ["Python", "Linux"],
        "lacks": ["Docker, SQL"],
        "fit_percent": 50
    }
    '''

    student_skillset = set(student)
    profession_skillset = set(profession)

    skills_stu_has = profession_skillset.intersection(student_skillset)
    skills_stu_lacks = profession_skillset.difference(student_skillset)

    fit_perset = len(skills_stu_has) / len(profession_skillset) * 100

    return {
        "has": list(skills_stu_has),
        "lacks": list(skills_stu_lacks),
        "fit_persent": fit_perset
    }
