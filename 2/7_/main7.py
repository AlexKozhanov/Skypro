import os
import utils7

student_past = os.path.join("data", "students.json")
profs_path = os.path.join("data", "professions.json")

def main():

    all_stidents = utils7.load_students(student_past)
    all_profs = utils7.load_students(profs_path)

    if not all_profs or not all_stidents:
        print("Данные не загрузились")
        return

    print("Введите номер студента")
    student_pk = int(input())
    student = utils7.get_student_by_pk(all_stidents, student_pk)

    if student == None:
        print('У нас нет такого студента')
        return

    print(f"Выберите специальность для оценки студента {student['full_name']}")
    prof_title = input()
    prof = utils7.get_profession_by_title(all_profs, prof_title)

    if prof == None:
        print('У нас нет такой специальности')
        return

    student_skills = student["skills"]
    prof_skills = prof["skills"]

    fitness = utils7.check_fitness(student_skills, prof_skills)

    student_skills_print = ", ".join(student['skills'])
    print(f"Студент {student['full_name']}")
    print(f"Знает {student_skills_print}")

    student_skill_has = ", ".join(fitness['has'])
    student_skill_lacks = ", ".join(fitness['lacks'])
    print(f"Пригодность {fitness['fit_persent']}%")
    print(f"{student['full_name']} знает {student_skill_has}")
    print(f"{student['full_name']} не знает {student_skill_lacks}")


if __name__ == '__main__':
    main()