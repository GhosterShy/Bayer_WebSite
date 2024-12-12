import asyncio
from django.core.management.base import BaseCommand
from Fastaiogram import main  # Импорт функции main из вашего бота

class Command(BaseCommand):
    help = "Запуск Telegram-бота"

    def handle(self, *args, **kwargs):
        self.stdout.write("Запуск Telegram-бота...")
        try:
            asyncio.run(main())
        except KeyboardInterrupt:
            self.stdout.write("Бот остановлен.")
