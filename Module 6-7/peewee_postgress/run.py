from models import db, Student, Group, Teacher, Subject, Grade
from db_operations import (top_5_students, top_student_with_highest_average_score, average)


# Створення таблиць у базі даних
def create_tables():
    try:
        # db.connect - це метод, який встановлює з'єднання з базою даних.
        db.connect()
        # db.create_tables - це метод, який створює таблиці в базі даних.
        db.create_tables([Student, Group, Teacher, Subject, Grade], safe=True)
        print("Tables created")

    # except Exception as e - це блок, який відловлює будь-які винятки, які виникають під час виконання коду.
    except Exception as e:
        print(e)

    # finally - це блок, який виконується завжди, навіть якщо виникає виняток.
    finally:
        # db.close - це метод, який закриває з'єднання з базою даних.
        db.close()


if __name__ == "__main__":
    create_tables()
    # populate_db()
    top_5_students()
    top_student_with_highest_average_score()
    average()


