<h2 align="center">API YAMDB</h2>

## О проекте

Проект YaMDb собирает отзывы пользователей на произведения.

Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка».
Список категорий может быть расширен.
Произведению может быть присвоен жанр из списка предустановленных (например,
«Сказка», «Рок» или «Артхаус»).

Добавлять произведения, категории и жанры может только администратор.
Благодарные или возмущённые пользователи оставляют к произведениям текстовые
отзывы и ставят произведению оценку в диапазоне от одного до десяти
(целое число); из пользовательских оценок формируется усреднённая оценка
произведения — рейтинг (целое число). На одно произведение пользователь может
оставить только один отзыв.

Пользователи могут оставлять комментарии к отзывам.
Добавлять отзывы, комментарии и ставить оценки могут только
аутентифицированные пользователи.

Документацию к API можно найти по адресу:

🔗 [<<ваш сервер или хостинг>>/redoc](http://localhost:8000/redoc/)
после запуска проекта.

## Проект выполнялся в команде из 3 человек

- 👋 [Кирилл Насонкин](https://github.com/kirill-nasonkin)
- 👋 [Лев Алексеев](https://github.com/heroinboy)
- 👋 [Ростислав Рыманов](https://github.com/RostIiIslav)

## Технологии

<img align="right" alt="GIF" src="https://oskolnews.ru/wp-content/uploads/2021/06/29.jpg" width="420" height="320" />

### Back-end

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)

![Django Rest Framework](https://img.shields.io/badge/DRF-red?style=flat-square&logo=Django)

### Database

![sqlite3](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

### Tools

![vscode](https://img.shields.io/badge/PyCharm-000000.svg?&style=for-the-badge&logo=PyCharm&logoColor=white)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)

![Postman](https://img.shields.io/badge/Postman-FCA121?style=flat-square&logo=postman)
![Git](https://img.shields.io/badge/-Git-black?style=flat-square&logo=git)
![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=github)

### Colaboration

![PR_closed](https://img.shields.io/github/issues-pr-closed/kirill-nasonkin/api_yamdb.svg)

## Как запустить проект

- Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone https://github.com/kirill-nasonkin/api_yamdb.git
cd api_yamdb
```

- Cоздать и активировать виртуальное окружение:

```bash
Unix
python3 -m venv env
source env/bin/activate
Windows
python -m venv env
source env/Scripts/activate
```

- Установить зависимости из файла requirements.txt:

```bash
Unix
python3 -m pip install --upgrade pip
Windows
python -m pip install --upgrade pip

pip install -r requirements.txt

```

- Выполнить миграции:

```bash
cd api_yamdb
Unix
python3 manage.py migrate
Windows
python manage.py migrate
```

- *Дополнительно* Для автоматического наполнения БД из csv файлов в папке
project_root/static/data применить команду:

```bash
Unix
python3 manage.py fill_my_db
Windows
python manage.py fill_my_db
```

- Запустить проект:

```bash
Unix
python3 manage.py runserver
Windows
python manage.py runserver
```
