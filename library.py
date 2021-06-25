from tkinter import *
import sqlite3


#====================
#====BACK END
#====================

#STEP 1: CREATE (DATABASE
def create_library():
  conn=sqlite3.connect("library.db")
  cur=conn.cursor()
  cur.execute("CREATE TABLE IF NOT EXISTS library(Title TEXT, Year INTERGER, Author TEXT, ISBN INTERGER )")
  conn.commit()
  conn.close

#STEP 2: COMMIT CHANGES TO THE DATABASE/ ADD A BOOK ENTRY
def insert(Title, Year, Author, ISBN):
  conn=sqlite3.connect("library.db")
  cur=conn.cursor()
  cur.execute("INSERT INTO library VALUES(?,?,?)",(Title, Year, Author, ISBN))
  conn.commit()
  conn.close

def add_entry():
  print(entry1_value.get())
  library_books.insert(END, entry1_value.get())
  
#====================
#====FRONT END
#====================



#CREATE THE BASE WINDOW
window=Tk()       

window.geometry("1200x600")
#set window color
window.configure(bg='cornflowerblue')
window.title("Your Favorite Books")
#window title
header = Label(window, text= "Your Favorite Books")
header.config(font=("Courier", 26))
header.grid(row=0, column=1)



#VIEW ALL BUTTON
button1=Button(window,text="View All", height=1,width=15 )
button1.grid(row=4,column=9 )
#SEARCH ENTRY BUTTON
button2=Button(window,text="Search Library ", height=1,width=15)
button2.grid(row=5,column=9 )
#ADD ENTRY BUTTON
button3=Button(window,text="Add Entry", command=add_entry, height=1,width=15 )
button3.grid(row=6,column=9 )
#UPDATE SELECTED BUTTON
button4=Button(window, text="Update Selected", height=1,width=15 )
button4.grid(row=7,column=9 )
#DELETE SELECTED BUTTON
button5=Button(window,text="Delete Selected", height=1,width=15)
button5.grid(row=8,column=9 )
#CLOSE PROGRAM BUTTON
button6=Button(window,text="Close Program", height=1,width=15)
button6.grid(row=9,column=9 )



#TITLE
title=Label(window, text="Title")
title.grid(row=6,column=0, padx=(20))
#title text box
title_value=StringVar()
title_entry=Entry(window, textvariable=title_value)
title_entry.grid(row=7,column=0, padx=(20))

#AUTHOR
author=Label(window, text="Author",)
author.grid(row=6,column=1)
#author text box
author_value=StringVar()
author_entry=Entry(window, textvariable=author_value)
author_entry.grid(row=7,column=1)


#CATEGORY
category=Label(window, text="Category", padx=(1))
category.grid(row=8,column=0)
#category text box
category_value=StringVar()
category_entry=Entry(window, textvariable=category_value)
category_entry.grid(row=9,column=0)
#ISBN
isbn=Label(window, text="ISBN", padx=(2))
isbn.grid(row=8,column=1)
#isbn text box
isbn_value=StringVar()
isbn_entry=Entry(window, textvariable=isbn_value)
isbn_entry.grid(row=9,column=1)








#LIST OF LIBRARY ENTRIES
library_books=Text(window, height=20,width=60)
library_books.grid(row=5,column=1, padx=(9))

#SCROLLBAR  
sb1=Scrollbar(window)
sb1.grid(row=5,column=5)
#ADD SCROLLBAR TO LIBRARY
library_books.configure(yscrollcommand=sb1.set)
sb1.configure(command=library_books.yview)







window.mainloop()

