"""
Build a library inventory desktop GUI Detabase App
"""

from tkinter import *
from GUI_backend import Database

database = Database()

def view_data():
    list.delete(0, END)
    for row in database.view():
        list.insert(END, row)

def search_data():
    list.delete(0, END)
    for row in database.search(title_v_value.get(), author_v_value.get(), year_v_value.get(), isbn_v_value.get()):
        list.insert(END, row)

def add_data():
    database.insert(title_v_value.get(), 
    author_v_value.get(), year_v_value.get(), isbn_v_value.get())
    list.delete(0, END)
    list.insert(END, (title_v_value.get(), 
    author_v_value.get(), year_v_value.get(), isbn_v_value.get()))

def delete_data():
    database.delete(selected_tuples[0])

def update_data():
    database.update(selected_tuples[0],title_v_value.get(), author_v_value.get(), year_v_value.get(), isbn_v_value.get())

def selected_row(event):
    try:
        global selected_tuples
        index = list.curselection()[0]
        selected_tuples = list.get(index)
        title_value.delete(0,END)
        title_value.insert(END, selected_tuples[1])
        author_value.delete(0,END)
        author_value.insert(END, selected_tuples[2])
        year_value.delete(0,END)
        year_value.insert(END, selected_tuples[3])
        isbn_value.delete(0,END)
        isbn_value.insert(END, selected_tuples[4])
    except IndexError:
        pass


window = Tk()
window.wm_title("Library View")

title=Label(window, text="Title")
title.grid(row=0, column=0)

title_v_value = StringVar()
title_value=Entry(window, textvariable=title_v_value)
title_value.grid(row=0, column=1)

author=Label(window, text="Author")
author.grid(row=0, column=2)

author_v_value = StringVar()
author_value=Entry(window, textvariable=author_v_value)
author_value.grid(row=0, column=3)

year=Label(window, text="Year")
year.grid(row=1, column=0)

year_v_value = StringVar()
year_value=Entry(window, textvariable=year_v_value)
year_value.grid(row=1, column=1)

isbn=Label(window, text="ISBN")
isbn.grid(row=1, column=2)

isbn_v_value = StringVar()
isbn_value=Entry(window, textvariable=isbn_v_value)
isbn_value.grid(row=1, column=3)

list = Listbox(window, height=9, width=35)
list.grid(row=2, column=0, rowspan=6, columnspan=2)

scrollbar = Scrollbar(window)
scrollbar.grid(row=2, column=2, rowspan=9)

list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=list.yview)

list.bind('<<ListboxSelect>>', selected_row)

btn_add = Button(window, text="Add", width=12, command=add_data)
btn_add.grid(row=2, column=3)

btn_update = Button(window, text="Update", width=12, command=update_data)
btn_update.grid(row=3, column=3)

btn_view = Button(window, text="View", width=12, command=view_data)
btn_view.grid(row=4, column=3)

btn_search = Button(window, text="Search", width=12, command=search_data)
btn_search.grid(row=5, column=3)

btn_delete = Button(window, text="Delete", width=12, command=delete_data)
btn_delete.grid(row=6, column=3)

btn_close = Button(window, text="Close", width=12, command=window.destroy)
btn_close.grid(row=7, column=3)

window.mainloop()