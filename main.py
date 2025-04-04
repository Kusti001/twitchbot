import random
import asyncio
import twitchio
from twitchio.ext import commands
from config import token

# Настройки
OAUTH_TOKEN = token
CHANNELS = ['Kusti0_0']  # Список каналов
MESSAGE_INTERVAL = 10  # Интервал в минутах

# Читаем строки из файла
with open("emotes.txt", encoding="utf-8") as f:
    MESSAGES = [line.strip() for line in f if line.strip()]

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=OAUTH_TOKEN, prefix='!', initial_channels=CHANNELS)

    async def event_ready(self):
        print(f'Бот запущен как {self.nick}')
        self.loop.create_task(self.send_random_messages())

    async def send_random_messages(self):
        while True:
            if MESSAGES:
                message = random.choice(MESSAGES)
                for channel in self.connected_channels:
                    await channel.send(message)
            await asyncio.sleep(MESSAGE_INTERVAL * 60)

bot = Bot()
bot.run()