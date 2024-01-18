FROM python:3.10.7

# Встановлюємо робочий каталог у контейнері
WORKDIR /app

# Копіюємо файли з поточного каталогу у робочий каталог контейнера
COPY . .

# Вказуємо, що контейнер слухає на певному порту в момент запуску.
# Це необов'язково, якщо ваша програма не слухає порт.
# EXPOSE 8000

# Команда, яка запускає вашу програму
CMD [ "python", "3.1_task.py" ]

# Команда, яка запускає вашу програму з аргументами
#docker stop my_zoo_app
#docker run -it --name my_zoo_app zoo_system