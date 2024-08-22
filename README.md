# Books API

Этот проект представляет собой API для управления книгами, авторами и продажами книг, написанный на Django и Django Rest Framework (DRF). Он также включает документацию API на основе Swagger.

## Установка и запуск проекта

Следуйте инструкциям ниже, чтобы установить и запустить проект на вашем локальном компьютере.

### Требования

- Python 3.12
- Django 5.1
- PostgreSQL

### Установка зависимостей

1. Клонируйте репозиторий:
    
bash
    git clone <URL вашего репозитория>
    cd ваш_репозиторий

2. Установите все зависимости с использованием [Poetry](https://python-poetry.org/):
    
bash
    poetry install

3. Создайте и примените миграции для создания необходимых таблиц:
    docker-compose exec web python backend/manage.py makemigrations
    docker-compose exec web python backend/manage.py migrate
    

5. Если у вас есть данные в формате фикстур, загрузите их:
    

### Запуск сервера разработки

Для запуска сервера разработки используйте команду:

docker-compose up --build

Теперь сервер доступен по адресу http://127.0.0.1:8000/.

## API Документация

Документация API доступна по следующим URL:
- Swagger UI: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
(ps допишу в выходные)

## Конфигурация

### Переменные окружения
Оставить так как есть осле клонирования 
либо
Создайте файл .env в корне проекта с содержанием:

dotenv
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/DB_NAME

### Примеры использования

**Получить список всех книг:**
http
GET /api/books/

**Получить список книг, опубликованных после 1 января 2023 года, которые доступны для покупки и стоимостью менее 30 тугриков:**
http
GET /api/books/published-after/

**Найти автора с наибольшим количеством опубликованных книг:**
http
GET /api/books/most-books-author/

**Рассчитать общий доход от продаж книг для каждого автора:**
http
GET /api/books/author-revenue/

**Получить список названий книг, в которых есть слово "Python":**
http
GET /api/books/containing-python/
