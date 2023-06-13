import sqlite3 as sq
from db import *

with sq.connect('base.db') as con:
    cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS authors(
  author_id INTEGER PRIMARY KEY,
  surname VARCHAR NOT NULL,
  name VARCHAR NOT NULL
  )""")

cur.execute("""CREATE TABLE IF NOT EXISTS books(
  book_id INTEGER PRIMARY KEY,
  name VARCHAR NOT NULL,
  section VARCHAR NOT NULL,
  publisher VARCHAR NOT NULL,
  publisher_date DATE NOT NULL,
  location VARCHAR NOT NULL,
  FOREIGN KEY (section) REFERENCES sections(section),
  FOREIGN KEY (publisher) REFERENCES publishers(publisher)
  )""")

cur.execute("""CREATE TABLE IF NOT EXISTS sections(
    id_section INT auto_increment PRIMARY KEY,
    section VARCHAR NOT NULL
    )""")

cur.execute("""CREATE TABLE IF NOT EXISTS publishers(
  publisher_id auto_increment PRIMARY KEY,
  publisher VARCHAR UNIQUE NOT NULL,
  city VARCHAR NOT NULL
  )""")

cur.execute("""CREATE TABLE IF NOT EXISTS author_book(
  author_book_id INTEGER PRIMARY KEY ,
  book_id INTEGER NOT NULL,
  author_id INTEGER NOT NULL,
  FOREIGN KEY (book_id) REFERENCES books(book_id),
  FOREIGN KEY (author_id) REFERENCES authors(author_id)
  )""")


cur.executemany("INSERT INTO authors VALUES (?, ?, ?)", authors)
cur.executemany("INSERT INTO books VALUES (?, ?, ?, ?, ?, ?)", books)
cur.executemany("INSERT INTO sections VALUES (?, ?)", sections)
cur.executemany("INSERT INTO publishers VALUES (?, ?, ?)", publishers)
cur.executemany("INSERT INTO author_book VALUES (?, ?, ?)", author_book)

#выборка
with sq.connect('base.db') as con:
    cur = con.cursor()
    print('Получить список всех книг, отсортированных по году издания:\n')
    for result in cur.execute("SELECT * FROM books ORDER BY publisher_date DESC\n"):
        print(result)

    print('\n')
    print('Получить список всех книг заданного автора:\n')
    for result in cur.execute("SELECT book_id FROM author_book WHERE author_id = 3\n"):
        print(result)

    print('\n')
    print('Получить список всех книг из заданного раздела:\n')
    for result in cur.execute("SELECT * FROM books WHERE section = 'Драма'\n"):
        print(result)

    print('\n')
    print('Получить список всех книг, изданных заданным издательством:\n')
    for result in cur.execute("SELECT * FROM books WHERE publisher = 'Эксмо'\n"):
        print(result)

    print('\n')
    print('Получить список всех авторов в алфавитном порядке:\n')
    for result in cur.execute("SELECT * FROM authors ORDER BY name"):
        print(result)

    print('\n')
    print('Получить список всех книг, отсортированных по названию и году издания:\n')
    for result in cur.execute("SELECT * FROM books ORDER BY name AND publisher_date = '1989'\n"):
        print(result)

    print('\n')
    print('Получить список всех книг заданного автора, отсортированных по году издания:\n')
    for result in cur.execute("SELECT * FROM books WHERE book_id = (SELECT book_id FROM author_book where author_id = 2) and publisher_date ORDER BY publisher_date DESC\n"):
        print(result)

    print('\n')
    print('Получить список всех книг, опубликованных в заданном году:\n')
    for result in cur.execute("SELECT * FROM books WHERE publisher_date = '2013'\n"):
        print(result)

    print('\n')
    print('Получить список всех авторов, написавших книги для заданного издательства:\n')
    for result in cur.execute("SELECT author_id FROM author_book WHERE book_id = (SELECT book_id FROM books where publisher = 'Речь')\n"):
        print(result)

    print('\n')
    print('Получить список всех книг, в названии которых есть заданное слово:\n')
    for result in cur.execute("SELECT * FROM books WHERE name LIKE '%ветер%'\n"):
        print(result)


# #обновление данных
with sq.connect('base.db') as con:
    cur = con.cursor()

# 1. Обновить год издания всех книг, написанных автором с фамилией "Иванов", установив год издания равным 2022:
cur.execute("""UPDATE books SET publisher_date = "2022" WHERE book_id IN (SELECT book_id FROM author_book JOIN authors ON author_book.author_id = authors.author_id WHERE surname = 'Иванов')""")
# 2. Обновить название и год издания книги, хранящейся в городе "Москва", установив название "Новая книга" и год издания равным 2023:
cur.execute("UPDATE books SET name = 'Новая книга', publisher_date = 2015 WHERE publisher IN (SELECT publisher FROM publishers WHERE city = 'Москва')")
# 3. Обновить название и раздел всех книг, написанных автором с именем "Александр" и фамилией "Петров", установив название "Новое название" и раздел "Фантастика":
cur.execute("""UPDATE books SET name = 'Новое название', section = (SELECT section FROM sections WHERE section = 'Фантастика') WHERE book_id IN (SELECT book_id FROM author_book JOIN authors ON author_book.author_id = authors.author_id WHERE name = 'Александр' AND surname = 'Петров')""")
# 4. Обновить название всех книг, которые были опубликованы в годы с 2010 по 2015 включительно, установив название "Старое название":
cur.execute("UPDATE books SET name = 'Старое название' WHERE publisher_date BETWEEN 2010 AND 2015")
# 5. Обновить место хранения всех книг, написанных автором с кодом 7, установив место хранения "Библиотека №2":
cur.execute("""UPDATE books SET location = 'Библиотека №2' WHERE book_id IN (SELECT book_id FROM author_book WHERE author_id = 7)""")
# 6. Обновление города из таблицы Издательства по коду города в таблице Книги:
cur.execute("""UPDATE publishers SET city = (SELECT city FROM books WHERE books.publisher = publishers.publisher)""")
# 7. Обновление кода автора в таблице АвторКниги по коду автора в таблице Авторы:
cur.execute("""UPDATE author_book SET author_id = (SELECT author_id FROM authors WHERE authors.author_id = author_book.author_id)""")
# 8. Обновление названия раздела в таблице Книги по названию раздела в таблице Разделы:
cur.execute("""UPDATE books SET section = (SELECT section FROM sections WHERE sections.section = books.section)""")
# 9. Обновление года издания в таблице Книги по году издания в таблице АвторКниги:
cur.execute("""UPDATE books SET publisher = '2022' WHERE book_id IN (SELECT book_id FROM author_book WHERE publisher = 2021)""")
# 10. Обновление места хранения в таблице Книги по названию издательства в таблице
cur.execute("""UPDATE books SET location = 'Публичная библиотека' WHERE publisher IN (SELECT publisher FROM publishers WHERE publisher = 'Время')""")
# 11. Обновление фамилии автора в таблице Авторы по коду автора в таблице АвторКниги:
cur.execute("""UPDATE authors SET surname = 'Новая фамилия' WHERE author_id IN (SELECT author_id FROM author_book WHERE author_id = 5)""")
# 12. Обновить год издания всех книг, изданных в городе "Москва", на 2022 год.
cur.execute("""UPDATE books SET publisher_date = '2022' WHERE publisher  IN (SELECT publisher  FROM publishers  WHERE city = 'Москва')""")
# 13. Обновить место хранения всех книг, написанных автором с фамилией "Иванов", на "Книжный шкаф 1".
cur.execute("""UPDATE books SET location = 'Книжный шкаф 1' WHERE book_id IN (SELECT book_id FROM author_book WHERE author_id IN (SELECT author_id FROM authors WHERE surname = 'Иванов'))""")
# 14. Обновить год издания всех книг, написанных автором с именем "Анна", на 2023 год.
cur.execute("""UPDATE books SET publisher_date = '2023' WHERE book_id IN (SELECT book_id FROM author_book WHERE author_id IN (SELECT author_id FROM authors WHERE name = 'Анна'))""")
# 15. Обновить название раздела всех книг, изданных в городе "Санкт-Петербург", на "Классика".
cur.execute("""UPDATE books SET section = 'Классика' WHERE publisher IN (SELECT publisher FROM publishers WHERE city = 'Санкт-Петербург')""")
# 16. Обновить год издания всех книг, написанных автором с фамилией "Петров", на 2024 год.
cur.execute("""UPDATE books SET publisher = '2024' WHERE book_id IN (SELECT book_id FROM author_book WHERE author_id IN (SELECT author_id FROM authors WHERE surname = 'Петров'))""")

#удаление данных
with sq.connect('base.db') as con:
    cur = con.cursor()

# 1. Удалить все записи из таблицы Книги, у которых Раздел = 'Фантастика':
cur.execute("DELETE FROM books WHERE section = 'Фантастика'")
# 2. Удалить все записи из таблицы Книги, у которых ГодИздания меньше 2000:
cur.execute("DELETE FROM books WHERE publisher_date < 2000")
# 3. Удалить все записи из таблицы АвторКниги, у которых КодАвтора равен 1:
cur.execute("DELETE FROM author_book WHERE author_id = 1")
# 4. Удалить все записи из таблицы Авторы, у которых Фамилия начинается с буквы "А":
cur.execute("DELETE FROM authors WHERE surname LIKE 'А%'")
# 5. Удалить все записи из таблицы Издательства, у которых Город равен "Москва":
cur.execute("DELETE FROM publishers WHERE city = 'Москва'")
# 6. Удалить все записи из таблицы АвторКниги, у которых КодКниги равен 10:
cur.execute("DELETE FROM author_book WHERE book_id = 10")
# 7. Удалить все записи из таблицы Книги, у которых МестоХранения равно "Склад":
cur.execute("DELETE FROM books WHERE location = 'Склад'")
# 8. Удалить все записи из таблицы Разделы, у которых Раздел равен "Детективы":
cur.execute("DELETE FROM sections WHERE section = 'Детектив'")
# 9. Удалить все записи из таблицы АвторКниги, у которых КодАвтора равен 2:
cur.execute("DELETE FROM author_book WHERE author_id = 2")
# 10. Удалить все записи из таблицы Издательства, у которых Издательство равно "O'Reilly Media":
cur.execute("DELETE FROM publishers WHERE publisher = 'OReilly Media'")
# 11. Удалить все записи из таблицы Книги, у которых Название содержит слово "Война":
cur.execute("DELETE FROM books WHERE name LIKE '%Война%'")
# 12. Удалить все книги, которые были изданы до 2000 года включительно, и которые хранятся в месте хранения "Библиотека №1".
cur.execute("DELETE FROM books WHERE publisher_date <= 2000 AND location = 'Библиотека №1'")
# 13. Удалить всех авторов, у которых нет книг в таблице Книги.
cur.execute("DELETE FROM authors WHERE author_id NOT IN (SELECT DISTINCT author_id FROM author_book)")
# 14. Удалить все книги, изданные в городе "Москва", из таблицы "Книги".
cur.execute("DELETE FROM books WHERE publisher IN (SELECT publisher FROM publishers WHERE city = 'Москва')")
# 15. Удалить всех авторов, чьи фамилии начинаются на букву "А" из таблицы "Авторы" и соответствующие записи из таблицы "АвторКниги".
cur.execute("DELETE FROM authors WHERE surname LIKE 'А%' AND author_id IN (SELECT author_id FROM author_book)")
cur.execute("DELETE FROM author_book WHERE author_id IN (SELECT author_id FROM authors WHERE surname LIKE 'А%')")
# 16. Удалить все записи из таблицы "АвторКниги", связанные с книгами, изданными в городе "Москва".
cur.execute("""DELETE FROM author_book WHERE book_id IN (SELECT book_id FROM books WHERE publisher IN (SELECT publisher FROM publishers WHERE city = 'Москва'))""")
# 17. Удалить все книги из таблицы "Книги", которые были написаны авторами, чьи фамилии начинаются на букву "П".
cur.execute("""DELETE FROM books WHERE book_id IN (SELECT book_id FROM author_book WHERE author_id IN (SELECT author_id FROM authors WHERE surname LIKE 'П%'))""")
# 18. Удалить все книги из таблицы "Книги", которые были изданы в городах, название которых начинается на букву "Н".
cur.execute("DELETE FROM books WHERE publisher IN (SELECT publisher FROM publishers WHERE city LIKE 'Н%')")
# 19. Удалить все записи из таблицы "АвторКниги", связанные с книгами, изданными в городах, название которых начинается на букву "Н".
cur.execute("""DELETE FROM author_book WHERE book_id IN (SELECT book_id FROM books JOIN publishers ON books.publisher = publishers.publisher WHERE publishers.city LIKE 'Н%')""")