## Module 4-5

### Завдання №1

*Реалізація простого ехо-сервера та ехо-клієнта з використанням сокетів
Мета: Створити дві програми - сервер та клієнт, які будуть використовувати TCP сокети для комунікації. 
Сервер буде приймати повідомлення від клієнта та відправляти йому назад те саме повідомлення (ехо).*

### Кроки:

### Написання ехо-сервера:

1. Створіть TCP сокет і зв'яжіть його з певним портом на вашому комп'ютері.
2. Нехай сервер слухає вхідні з'єднання.
3. Коли сервер приймає з'єднання від клієнта, він повинен читати повідомлення, що надійшло від клієнта.
4. Після отримання повідомлення, сервер повинен відправити назад це ж повідомлення (ехо).

### Написання ехо-клієнта:

1. Створіть TCP сокет.
2. Підключіть сокет до сервера, використовуючи той самий порт, на який сервер прив'язаний.
3. Відправте повідомлення серверу через сокет.
4. Отримайте відповідь від сервера та виведіть її на екран.

### Тестування:

1. Спочатку запустіть сервер, а потім клієнт.
2. Спробуйте відправити різні повідомлення від клієнта та перевірте, чи правильно сервер відправляє ехо-відповіді.
3. Це базове завдання допоможе вам зрозуміти, 
як працюють сокети та як можна налаштувати просту взаємодію між сервером та клієнтом.

### Завдання №2

*Асинхронний HTTP-клієнт
Мета: Створити асинхронний HTTP-клієнт, який здійснюватиме паралельні запити до кількох URL і збиратиме відповіді.*

### Кроки:
1. Написання асинхронної функції для запиту: Створіть асинхронну функцію `fetch`, яка приймає URL як аргумент і виконує HTTP-запит до цього URL за допомогою асинхронної бібліотеки, наприклад aiohttp.
2. Створення списку URL для запитів: Визначте список URL, до яких будуть здійснюватися запити. Це можуть бути різні веб-сайти або різні ендпойнти одного API.
3. Виконання паралельних запитів: Використайте `asyncio.gather` для виконання функції `fetch` паралельно для кожного URL зі списку.
4. Обробка відповідей: Виведіть відповіді сервера на кожен запит або обробіть їх належним чином.

### Підказки:
* Ви створюєте асинхронну функцію `fetch`, яка робить HTTP-запит.
* У функції `main` формуєте список URL і запускаєте асинхронні запити до кожного URL.
* Використовуєте `aiohttp` для асинхронних HTTP-запитів.
* Всі відповіді обробляються асинхронно та виводяться або обробляються за необхідності.

### Завдання №3

*Реалізація простого Aiohttp WebSocket-клієнта
Мета: Створити асинхронний WebSocket-клієнт за допомогою бібліотеки aiohttp, який з'єднається з WebSocket-сервером, відправить повідомлення та отримає відповідь.*

### Кроки:
1. Встановлення `aiohttp`: 
* Якщо у вас ще не встановлено `aiohttp`, 
виконайте команду `pip install aiohttp.`
2. Створення асинхронного WebSocket-клієнта:
* Використайте `aiohttp.ClientSession().ws_connect` для встановлення з'єднання з WebSocket-сервером.
* Відправте повідомлення на сервер після встановлення з'єднання.
* Отримайте та виведіть відповідь від сервера. 
3. Тестування з'єднання:
* Використайте публічний WebSocket-сервер або локальний сервер, якщо у вас є такий, для тестування клієнта.
* Переконайтеся, що ви можете відправляти та отримувати повідомлення.

### Підказки:
* Ви створюєте асинхронну функцію `websocket_client`, яка підключається до WebSocket-сервера.
* Використовується адреса wss://echo.websocket.org як приклад WebSocket-сервера, що відображає відправлені повідомлення.
* Відправляється тестове повідомлення "Hello, WebSocket!" на сервер.
* Отримується відповідь від сервера та виводиться на екран.