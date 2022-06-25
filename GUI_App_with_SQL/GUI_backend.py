import sqlite3, os
os.system("clear")

class Database:

    def __init__(self):
        self.connection = sqlite3.connect("gitProjects/GUI_App_with_SQL/library_store.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS library (id INTEGER PRIMARY KEY, \
        title text, author text, year integer, isbn integer)")
        self.connection.commit()

    def insert(self, title, author, year, isbn):
        self.cursor.execute("insert into library values (null,?,?,?,?)", (title, author, year, isbn))
        self.connection.commit()

    def view(self):
        self.cursor.execute("select * from library")
        row = self.cursor.fetchall()
        return row

    def search(self, title="", author="", year="", isbn=""):
        self.cursor.execute("select * from library where title =? or author=? or year=? or isbn=?", \
            (title, author, year, isbn))
        row = self.cursor.fetchall()
        return row

    def delete(self, id):
        self.cursor.execute("delete from library where id=?", (id,))
        self.connection.commit()

    def update(self, id, title, author, year, isbn):
        self.cursor.execute("update library set title=?, author=?, year=?, isbn=? where id=?", \
        (title, author, year, isbn, id))
        self.connection.commit()

    def __del__(self):
        self.connection.close()

# insert("The Progmatic Programmer", "David Thomas", 2009, 302348391)
# print("How many entries in a table: ",view())
# delete(1)
# print("\n")
# update(2,"","Harish Sharma", 1980, 939485)
# print("Searched entry: ", search(author="David Thomas"))
# print("\n")
# print("How many entries do we have in a table now: ",view())