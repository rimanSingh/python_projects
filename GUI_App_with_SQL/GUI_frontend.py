"""
Build a library inventory desktop GUI Detabase App
"""

from tkinter import *
import GUI_backend

window = Tk()

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

btn_add = Button(window, text="Add", width=12)
btn_add.grid(row=2, column=3)

btn_update = Button(window, text="Update", width=12)
btn_update.grid(row=3, column=3)

btn_view = Button(window, text="View", width=12)
btn_view.grid(row=4, column=3)

btn_search = Button(window, text="Search", width=12)
btn_search.grid(row=5, column=3)

btn_delete = Button(window, text="Delete", width=12)
btn_delete.grid(row=6, column=3)

btn_close = Button(window, text="Close", width=12)
btn_close.grid(row=7, column=3)

window.mainloop()