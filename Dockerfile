# Используем официальный базовый образ Python
FROM python:3.12

# Устанавливаем зависимости
RUN pip install --upgrade pip

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем requirements.txt в контейнер
COPY requirements.txt .

# Устанавливаем зависимости приложения
RUN pip install -r requirements.txt

# Копируем исходный код приложения в контейнер
COPY . .

# Открываем порт, на котором будет работать приложение
EXPOSE 8000

# Команда для запуска приложения
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]