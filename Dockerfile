FROM python:3.14-slim

WORKDIR /app

# 1. Копіюємо та встановлюємо залежності
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2. Явно копіюємо головний файл та папу з кодом
COPY main.py .
COPY app/ ./app/

EXPOSE 8000

# 3. Запуск сервера
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]