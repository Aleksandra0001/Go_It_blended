from models import Student, Group, Teacher, Subject, Grade, db
from faker import Faker
import random

faker = Faker()

def populate_db():
    try:
        db.connect()

        # Створення груп
        groups = [Group.create(name=f"Group {i}") for i in range(1, 4)]

        # Створення викладачів
        teachers = [Teacher.create(name=faker.name()) for i in range(5)]

        # Створення предметів
        subjects = [Subject.create(name=f"Subject {i + 1}", teacher=random.choice(teachers)) for i in range(8)]

        # Створення студентів та оцінок
        # Для кожного студента створюємо випадкову кількість оцінок з випадковими предметами та випадковими балами
        for _ in range(50):
            # Вибираємо випадкову групу
            student = Student.create(name=faker.name(), group=random.choice(groups))
            # Для кожного студента створюємо випадкову кількість оцінок
            for subject in subjects:
                # Випадкова кількість оцінок від 5 до 20
                for _ in range(random.randint(5, 20)):
                    # Випадковий бал від 60 до 100
                    Grade.create(
                        student=student,
                        subject=subject,
                        score=random.randint(60, 100),
                        # Випадкова дата від 1 року тому до сьогодні
                        date=faker.date_between(start_date='-1y', end_date='today')
                    )

        print("Database populated with random data")

    except Exception as e:
        print(e)

    finally:
        db.close()

