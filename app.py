import os
from dotenv import load_dotenv

# Загружает переменные из файла .env в окружение системы
load_dotenv()

# Получает значение ключа
api_key = os.getenv('API_TOKEN')

print(f"Ключ загружен: {api_key[:4]}...") # Печатаем только начало для безопасности
