import concurrent.futures  # Для створення паралельних обчислень за допомогою процесів.
import logging  # Для логування.
import time  # Для вимірювання часу виконання.
from multiprocessing import Pool, current_process, cpu_count  # Для створення пулу процесів та отримання кількості ядер.


# Синхронна версія функції factorize.
def factorize(numbers: list) -> list:
    result_list = []  # Результат.
    for number in numbers:  # Для кожного числа в списку.
        temp_list = []  # Тимчасовий список для зберігання дільників поточного числа.
        for num in range(1, number + 1):  # Перебір чисел для знаходження дільників.
            if number % num == 0:  # Якщо num є дільником number.
                temp_list.append(num)  # Додаємо дільник до тимчасового списку.
        result_list.append(temp_list)  # Додаємо тимчасовий список дільників до результату.
    return result_list  # Повертаємо результат.


# Паралельна версія функції factorize для одного числа.
def factorize_multy(number: int) -> list:
    result_list = []  # Результат.
    for num in range(1, number + 1):  # Перебір чисел для знаходження дільників.
        if number % num == 0:  # Якщо num є дільником number.
            result_list.append(num)  # Додаємо дільник до результату.
    return result_list  # Повертаємо результат.


# Точка входу в програму.
if __name__ == "__main__":
    lst = [128, 255, 99999, 10651060, 123142342, 345345345]
    # Вимірювання часу виконання синхронної версії.
    start_time = time.time()
    a, b, c, d, *_ = factorize(lst)
    end_time = time.time()
    print(f"Sync time is: {end_time - start_time}")

    # Конфігурація логера.
    logger = logging.getLogger()
    stream_handler = logging.StreamHandler()
    logger.addHandler(stream_handler)
    logger.setLevel(logging.DEBUG)

    count_core = cpu_count()  # Кількість доступних ядер.

    # Вимірювання часу виконання паралельної версії за допомогою Pool.
    start_time_multy = time.time()
    with Pool(processes=count_core) as pool:
        logger.debug(pool.map(factorize_multy, lst))
    end_time_multy = time.time()
    print(f"Multy_pool time is: {end_time_multy - start_time_multy}")

    # Вимірювання часу виконання паралельної версії за допомогою concurrent.futures.
    start_time_multy2 = time.time()
    with concurrent.futures.ProcessPoolExecutor(count_core) as executor:
        executor.map(factorize_multy, lst)
    end_time_multy2 = time.time()
    print(f"Sync time mylty concarent is: {end_time_multy2 - start_time_multy2}")
