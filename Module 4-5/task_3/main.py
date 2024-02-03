import aiohttp
import asyncio

""""Оголошуємо асинхронну функцію websocket_client, яка буде виконувати логіку нашого WebSocket-клієнта."""
async def websocket_client():
    """"Використовуючи асинхронний контекстний менеджер, створюємо сесію клієнта.
     Це дає нам можливість виконувати HTTP-запити і встановлювати WebSocket-з'єднання."""""
    async with aiohttp.ClientSession() as session:
        """"Відкриваємо асинхронне з'єднання з WebSocket-сервером. 
        Використовуємо URL wss://echo.websocket.org як приклад."""
        async with session.ws_connect('wss://echo.websocket.org') as ws:
            """"Асинхронно відправляємо рядкове повідомлення "Hello, WebSocket!" 
            на сервер через відкрите WebSocket-з'єднання."""
            await ws.send_str("Hello, WebSocket!")
            """"Асинхронно чекаємо на відповідь від сервера."""
            msg = await ws.receive()
            print(f"Message from server: {msg.data}")

if __name__ == "__main__":
    asyncio.run(websocket_client())
