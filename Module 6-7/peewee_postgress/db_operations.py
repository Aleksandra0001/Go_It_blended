from models import Student, Grade, Subject, Group, Teacher
from peewee import *


# Знайти 5 студентів із найбільшим середнім балом з усіх предметів
# fn.AVG(Grade.score).alias('average_score') - це функція, яка обчислює середній бал для кожного студента
# fn - це модуль, який містить функції для виконання операцій в базі даних, такі як fn.AVG, fn.SUM, fn.COUNT тощо.
# join(Grade) - це метод, який вказує, що потрібно з'єднати таблицю Student з таблицею Grade.
# group_by(Student) - це метод, який групує дані за полем Student.
# order_by(fn.AVG(Grade.score).desc()) - це метод, який сортує дані за середнім балом в порядку спадання.
# limit(5) - це метод, який обмежує кількість записів, які повертаються.
# alias('average_score') - це метод, який вказує, що середній бал повинен зберігатися під псевдонімом average_score.
# asc() - це метод, який сортує дані в порядку зростання, а desc() - в порядку спадання.
def top_5_students():
    top_students = (Student
                    .select(Student, fn.AVG(Grade.score).alias('average_score'))
                    .join(Grade)
                    .group_by(Student)
                    .order_by(fn.AVG(Grade.score).desc())
                    .limit(5))

    for student in top_students:
        print(f"Top 5 students: {student.name} - {student.average_score}")


# Знайти студента із найвищим середнім балом з певного предмета (наприклад, з предмета "Subject 1")
def top_student_with_highest_average_score():
    subject = Subject.get(Subject.name == "Subject 1")
    top_student = (Student
                   .select(Student, fn.AVG(Grade.score).alias('average_score'))
                   .join(Grade)
                   .where(Grade.subject == subject)
                   .group_by(Student)
                   .order_by(fn.AVG(Grade.score).desc())
                   .limit(1)
                   .get())
    print(f"Top student for {subject.name}: {top_student.name} - {top_student.average_score}")

# Знайти середній бал на потоці (по всій таблиці оцінок):
def average():
    overall_average = (Grade
                       .select(fn.AVG(Grade.score).alias('average_score'))
                       .get())

    # average_score - це псевдонім, під яким зберігається середній бал.
    print(f"Overall average score: {overall_average.average_score}")

