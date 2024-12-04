# Используем официальный образ Python
FROM python:3.12

# Устанавливаем рабочую директорию
WORKDIR /travelo

# Копируем файлы проекта в контейнер
COPY . /travelo/

# Обновляем pip и устанавливаем setuptools
RUN pip install --upgrade pip setuptools

RUN apt-get update && apt-get install -y redis-tools telnet
#RUN apt-get update && apt-get install -y redis-tools rabbitmq-server

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r install.txt

# Выполняем команду collectstatic
RUN python manage.py collectstatic --noinput

# Применяем миграции
RUN python manage.py migrate

# Открываем порт, на котором будет работать приложение
EXPOSE 8000

# Команда для запуска приложения с Uvicorn и collectstatic
CMD ["sh", "-c", "python manage.py collectstatic --noinput && gunicorn travelo.wsgi:application"]
