## Module 6-7

### Peewee ORM ([Peewee documentation](http://docs.peewee-orm.com/en/latest/))

*`Peewee` — це легкий ORM (Object-Relational Mapping) інструмент для Python, 
який дозволяє працювати з базами даних, використовуючи класи та об'єкти Python, 
а не прямі SQL-запити.* 

#### Основні характеристики Peewee:
- Підтримка багатьох баз даних, включаючи `SQLite`, `MySQL` і `PostgreSQL`.
- Невеликий розмір та легкість використання.
- Можливість виконання запитів за допомогою зрозумілого, "пітонічного" синтаксису.
- Вбудовані інструменти для підтримки міграцій баз даних.

#### Встановлення Peewee:
`pip install peewee`

#### [Типи полів Peewee](https://peewee.readthedocs.io/en/latest/peewee/models.html#field-types-table)

#### Ініціалізуючі аргументи

*Кожне поле приймає наступні ініціалізуючі аргументи:*
- `null=False` – чи можливо зберігати null-значення;
- `index=False` – створювати чи індекс для даного стовпця в базі;
- `unique=False` – створювати чи унікальний індекс для даного стовпця в базі.;
- `verbose_name=None` – рядок для відображення назви поля;
- `help_text=None` – рядок з допоміжним текстом для поля;
- `db_column=None` – рядок, явно задаючий назву стовпця в базі для даного поля;
- `default=None` – значення за замовчуванням для полів класу при створенні нового об'єкта;
- `choices=None` – список або кортеж двоелементних кортежів, де перший елемент – значення для бази, 
другий – відображуване значення (аналогічно до Django);
- `primary_key=False` – використовувати чи дане поле як первинний ключ;
- `sequence=None` – послідовність для наповнення поля (переконайтеся, що бекенд підтримує таку функціональність).

#### Метадані

*Для кожної таблиці можна прописати єдині метадані в class Meta:*

| Опція         | Опис                                                            | Наслідується? |
|---------------|-----------------------------------------------------------------|---------------|
| `database`    | База даних для моделі                                           | Так           |
| `db_table`    | Назва таблиці, в якій будуть зберігатися дані                   | Ні            |
| `indexes`     | Список полів для індексації                                     | Так           |
| `order_by`    | Список полів для сортування за замовчуванням                    | Так           |
| `primary_key` | Складовий первинний ключ, екземпляр класу CompositeKey, приклад | Так           |
| `table_alias` | Аліас таблиці для використання в запитах                        | Ні            |

