# weather-scrapper

## О проекте

Данный проект выполняет скрапинг и сравнение предсказываемой и реальной погоды с
сайта http://www.chelpogoda.ru

## Зависимости

- Docker

## Сборка проекта

### build.sh

- Клонируйте данный репозиторий и перейдите в папку с ним
- Запустите из терминала установочный скрипт _**build.sh**_ и
  проследуйте за шагами на экране (Введите логин и пароль для новой базы данных).
  Перед запуском убедитесь, что у пользователя есть права на создание docker-контейнеров.

```bash
./build.sh
```

Далее можете перейти на главную страницу сайта по адресу http://localhost:8000/
и наслаждаться работой данного сервиса.

### Docker compose

- Клонируйте данный репозиторий и перейдите в папку с ним
- Создайте .env файл, в котором будет содержаться
  информация о создаваемой базе данных

```
DB_USER=<username>
DB_PASSWORD=<password>
```

- Убедитесь, что файл лежит в корне проекта и имеет правда на чтение
- Запустите контейнеры

```bash
docker compose up
```

- Перейдите на главную страницу сервиса http://localhost:8000/

## Отказ от ответственности

Данный проект был написан исключительно в образовательных целях.
Автор не несет никакой ответственности за использование данного продукта сторонними
лицами. Все правда принадлежат их правообладателям в т.ч. сайту chelpogoda.ru