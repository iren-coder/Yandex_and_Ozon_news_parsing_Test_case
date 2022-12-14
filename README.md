Тестовое задание для Backend-разработчика


Видеоскринкаст находится в корневой папке репозитория

1. <em>Задание</em>: Парсер // Спарсить первые 10 новостей со следующих ресурсов, проставить тэги (ozon, yandex).
Яндекс.Маркет — https://market.yandex.ru/partners/news 
OZON — https://seller.ozon.ru/news/ 
Новостям проставить основные тэги по названиям ресурсов и внутренние тэги, которые есть в новостях типа fbo, fbs, realfbs, аналитика и т.п.

<em>Что сделано</em> : Парсер parser.py заходит на означенные ресурсы и собирает данные по последним 10-ти новостям. Данные сохраняются в csv файлы, которые затем переносятся в БД. Таблица <srtong>News</strong> предназначена для хранения всех данных по новостям и имеет структуру со следующими колонками:
- id - id новости, primery key
- title - заголовок новости
- content - содержимое новости
- date - дата новости
- tag - тэги новости
- canal - источник новости (Y = Yandex, O = Ozon)<br>

Со скраппингом новостей с OZON пришлось повозиться, т.к. там анти-бот. Смотрите <strong>parser.py</em><br>

<em>Работа парсера</em>

![Работа парсера](/screenshots/Parser_works.png)

<em>Пример таблицы</em>

![Пример таблицы](/screenshots/Table.png)

2. <em>Задание</em> : Админка // Сделать на Django админку для новостей с шаблоном Admin LTE 3 и занести данные из парсера в базу MySQL.

<em>Что сделано</em> : Пенель администратора настроена в соответствии с шаблоном Admin LTE 3.<br>

<em>Панель администратора. Стартовая страница</em>
![Панель администратора. Стартовая страница](/screenshots/admin.png)

<em>Добавление новости из панели администратора</em>
![Добавление новости из панели администратора](/screenshots/admin2.png)

3. <em>Задание:</em>  API // Сделать простой API запрос для frontend на получение структурированных новостей в формате JSON:
— все новости по дате,
— отдельно каналы/новости по тэгам.

<em>Что сделано:</em><br>
Фильтрация осуществляется по дате, тэгу, каналу (Яндекс или Озон)

Для фильтрации новости по дате пользуйтесь кнопкой Filters REST-интерфейса либо вбейте в строке браузера
http://localhost/api/v1/newslist/?search=date<br>
например, чтобы получить все новости за 25 августа:<br>
http://localhost/api/v1/newslist/?search=2022-08-25

Для фильтрации новости по тэгу пользуйтесь кнопкой Filters REST-интерфейса либо вбейте в строке браузера
http://localhost/api/v1/newslist/?search=tag<br>
например, чтобы получить все новости с тэгом FBS:<br>
http://localhost/api/v1/newslist/?search=fbs

Для фильтрации новости по источнику новости (Яндекс canal=y, OZON canal=o) пользуйтесь кнопкой Filters REST-интерфейса 
либо вбейте в строке браузера
http://localhost/api/v1/newslist/?search=canal<br>
например, чтобы получить все новости от OZON:<br>
http://localhost/api/v1/newslist/?search=o<br>

<em>API список всех новостей</em>
![API список всех новостей](/screenshots/newslist.png)

<em>Фильтрация новостей</em>
![Фильтрация новостей](/screenshots/filter.png)

<em>Задание:</em> Срок исполнения — 2 календарных дня<br>
<em>Что сделано:</em> Работа над проектом заняла 2 календарных дня с учётом серьёзной подготовки к 1 сентября))))<br>

Проект разработан на основе фреймворка Django, используемая БД Postgres, вёрстка на основе Bootstrap 4.

<em>Как развернуть приложение локально:</em>

1. Создайте виртуальное окружение в папке, куда планируете скачать проект:<br>
<em>python -m venv</em><br>
(например, python -m venv C:\User\project)

2. Активируйте виртуальное окружение командой<br> <em>cd C:\Users\project\Scripts\activate.bat</em>

3. Скачайте проект по ссылке <br><strong>https://github.com/iren-coder/Yandex_and_Ozon_news_parsing_Test_case</strong> <br>либо склонируйте репозиторий <br><strong>git@github.com:iren-coder/Yandex_and_Ozon_news_parsing_Test_case</strong>.

4. Установите Postgres и создайте базу данных Postgres, создайте юзера с именем и паролем и дайте ему все привилегии над базой. Затем впишите свои название БД, имя юзера и пароль в раздел DATABASES в файле my_project/settings.py<br>
- установка PostgreSQL: <em>sudo apt install postgresql postgresql-contrib</em>
- войти в консоль postgres: <em>sudo -u postgres psql</em>
- создать базу данных и пользователя:
        - CREATE DATABASE db_name;
        - CREATE USER user_name WITH PASSWORD 'password';
- дать все разрешения пользователю для работы с базой данных: GRANT ALL PRIVILEGES ON DATABASE db_name TO user_name;

5. Создайте и примените миграции:
<em>python manage.py makemigrations</em>
<em>python manage.py migrate</em>

6. Скопируйте статические файлы <em>python manage.py collectstatic</em>

7. Чтобы пользоваться панелью администратора, создайте суперюзера <em>python manage.py createsuperuser<em>

8. Запустите сервер <em>python manage.py runserver</em>

9. Запустите парсер </em>python parser.py</em>
10. Собранные данные будут сохранены в два файла yandex_data.csv и ozon_data.csv. Скопируйте данные в БД. Например, 

<em>\COPY data_base_name FROM ‘C:\ozon_data.csv’ DELIMITER ‘,’ CSV HEADER;</emS>

11. Для тестирования Вы также можете создать и сохранить любую новость сомостоятельно через панель администратора.


