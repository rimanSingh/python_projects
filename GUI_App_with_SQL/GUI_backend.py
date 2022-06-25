import sqlite3, os
os.system("clear")

def dbconnect():
    connection = sqlite3.connect("gitProjects/GUI_App_with_SQL/library_store.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS library (id INTEGER PRIMARY KEY, \
    title text, author text, year integer, isbn integer)")
    connection.commit()
    connection.close()

def insert(title, author, year, isbn):
    connection = sqlite3.connect("gitProjects/GUI_App_with_SQL/library_store.db")
    cursor = connection.cursor()
    cursor.execute("insert into library values (null,?,?,?,?)", (title, author, year, isbn))
    connection.commit()
    connection.close()

def view():
    connection = sqlite3.connect("gitProjects/GUI_App_with_SQL/library_store.db")
    cursor = connection.cursor()
    cursor.execute("select * from library")
    row = cursor.fetchall()
    connection.close()
    return row

def search(title="", author="", year="", isbn=""):
    connection = sqlite3.connect("gitProjects/GUI_App_with_SQL/library_store.db")
    cursor = connection.cursor()
    cursor.execute("select * from library where title =? or author=? or year=? or isbn=?", \
        (title, author, year, isbn))
    row = cursor.fetchall()
    connection.close()
    return row

def delete(id):
    connection = sqlite3.connect("gitProjects/GUI_App_with_SQL/library_store.db")
    cursor = connection.cursor()
    cursor.execute("delete from library where id=?", (id,))
    connection.commit()
    connection.close()

def update(id, title, author, year, isbn):
    connection = sqlite3.connect("gitProjects/GUI_App_with_SQL/library_store.db")
    cursor = connection.cursor()
    cursor.execute("update library set title=?, author=?, year=?, isbn=? where id=?", \
        (title, author, year, isbn, id))
    connection.commit()
    connection.close()

dbconnect()

insert("The Progmatic Programmer", "David Thomas", 2009, 302348391)
print("How many entries in a table: ",view())
# delete(1)
print("\n")
# update(2,"","Harish Sharma", 1980, 939485)
# print("Searched entry: ", search(author="Manish"))
# print("\n")
# print("How many entries do we have in a table now: ",view())
print("\n")