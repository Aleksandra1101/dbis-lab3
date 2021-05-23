# dbis-lab3
В лабораторній роботі було створено веб-застосунок, який представляє собою редактор творів української літератури.
1.1. Організація CRUD-операцій:
Веб-застосунок дає можливість зчитувати дані, видаляти існуючі та записувати нові. Операції реалізовано завдяки функціоналу SQLAlchemy.

1.2. Робота з сутностями:
Сутності - Автор, Книга

Сутність Автор має такі атрибути:
-ім'я;
-місто, в якому народився;

Сутність Книга має такі атрибути:
-заголовок;
-рік видання;
-ім'я автора;

2. Отримати навички роботи з веб-фреймворками
   Організація бізнес-логіки на сервері  файл start.py містить усю бізнес-логіку, що включає:
-завантаження пісні на сервер;
-редагування даних про пісню;

3. Отримати навички розбиття системи на слої
Система складається з чотирьох слоїв:

-database layer - БД Postresql.
-persistence layer - зв'язок з БД.
-business layer - файл start.py містить усю бізнес-логіку.
-presentation layer - html-файл складає користувацький інтерфейс.

4. Навчитись розгортати систему на хмарному хостингу
Систему розгорнуто на хмарному хостингу Heroku: https://flask-libr.herokuapp.com/

5. Розвинути навички моделювання даних, створення ERD та проєктуванням БД
Усе це було виконано при проектуванні, створенні та розгортанні веб-застосунку.

Інструкція з розгортання
У папці з проєктом ініціалізувати git-репозиторій
-Увійти в Heroku-акаунт (через heroku login).
-(git add .; git commit -am "some message"; git push heroku master)






