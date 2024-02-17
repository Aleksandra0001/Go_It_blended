from peewee import *
from dotenv import dotenv_values

# Завантаження конфігурації з .env файлу
config = dotenv_values("../.env")

# Підключення до бази даних
db = PostgresqlDatabase(
    config.get("POSTGRES_DB"),
    user=config.get("POSTGRES_USER"),
    password=config.get("POSTGRES_PASSWORD"),
    host=config.get("POSTGRES_HOST"),
    port=config.get("POSTGRES_PORT")
)


# Створення class BaseModel, щоб всі моделі успадковували його,
# і ми могли вказати базу даних для всіх моделей один раз.
class BaseModel(Model):
    class Meta:
        database = db


# Створення моделі Group, яка приймає BaseModel в якості батьківського класу та має поле name.
class Group(BaseModel):
    name = CharField()

    # Внутрішній клас Meta, який вказує, що модель Group повинна зберігатися в таблиці groups.
    class Meta:
        table_name = "groups"


# Створення моделі Student, яка приймає BaseModel в якості батьківського класу та має поле name.
class Student(BaseModel):
    name = CharField()
    group = ForeignKeyField(Group, backref='students')

    class Meta:
        table_name = "students"

# Створення моделі Teacher, яка приймає BaseModel в якості батьківського класу та має поле name.
class Teacher(BaseModel):
    name = CharField()

    # Внутрішній клас Meta, який вказує, що модель Teacher повинна зберігатися в таблиці teachers.
    class Meta:
        table_name = "teachers"


# Створення моделі Subject, яка приймає BaseModel в якості батьківського класу та має поле name та teacher,
# яке є ForeignKeyField, що посилається на модель Teacher та має backref="subjects". backref - це зворотній зв'язок,
# який дозволяє отримати всі предмети, які викладає вчитель.
class Subject(BaseModel):
    name = CharField()
    teacher = ForeignKeyField(Teacher, backref="subjects")

    # Внутрішній клас Meta, який вказує, що модель Subject повинна зберігатися в таблиці subjects.
    class Meta:
        table_name = "subjects"

# Створення моделі StudentGroup, яка приймає BaseModel в якості батьківського класу та має поля student, subject,
# score та date. Поля student та subject є ForeignKeyField, які посилаються на моделі Student та Subject відповідно.
class Grade(BaseModel):
    student = ForeignKeyField(Student, backref='grades')
    subject = ForeignKeyField(Subject, backref='grades')
    score = IntegerField()
    date = DateField()

    # Внутрішній клас Meta, який вказує, що модель Grade повинна зберігатися в таблиці grades.
    class Meta:
        table_name = "grades"

# def peewee_migration():
#     # Створення таблиць в базі даних
#     db.create_tables([Student, Group, Teacher, Subject, Grade])
#     # Закриття з'єднання з базою даних
#     db.close()
