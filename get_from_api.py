from newsapi import NewsApiClient
import os
from dotenv import load_dotenv

# Загружает переменные из файла .env в окружение системы
load_dotenv()

# Получает значение ключа
api_key = os.getenv('API_TOKEN')
api = NewsApiClient(api_key=api_key)
