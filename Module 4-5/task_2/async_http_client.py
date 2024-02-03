import aiohttp
import asyncio

"""Оголошуємо асинхронну функцію fetch, яка приймає об'єкт сесії (session) та URL."""
async def fetch(session, url):
    """"Виконуємо асинхронний GET-запит до заданого URL за допомогою сесії aiohttp. 
    Використання async with забезпечує правильне закриття відповіді після її обробки."""""
    async with session.get(url) as response:
        """"Отримуємо текстову відповідь з сервера та повертаємо її разом з URL."""
        return await response.text(), url

""""Оголошуємо головну асинхронну функцію, яка приймає список URL."""
async def main(urls):
    """Створюємо асинхронну сесію для виконання HTTP запитів."""""
    async with aiohttp.ClientSession() as session:
        """"Створюємо список асинхронних завдань для кожного URL."""
        tasks = [fetch(session, url) for url in urls]
        """"Використовуємо asyncio.gather для паралельного виконання всіх задач."""
        responses = await asyncio.gather(*tasks)
        """Проходимося по кожній відповіді, виводячи URL та перші 100 символів відповіді."""
        for response, url in responses:
            print(f"Response from {url}:\n{response[:100]}\n")  # Виводимо перші 100 символів відповіді

if __name__ == "__main__":
    urls = ["http://python.org", "https://openai.com"]  # Список URL для запитів
    asyncio.run(main(urls))
