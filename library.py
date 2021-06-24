from tkinter import *
import sqlite3


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

window.geometry("800x500")
#set window color
window.configure(bg='cornflowerblue')


#VIEW ALL BUTTON
button1=Button(window,text="View All", height=1,width=15 )
button1.grid(row=4,column=5 )
#SEARCH ENTRY
button2=Button(window,text="Search Library ", height=1,width=15, pady=(10))
button2.grid(row=5,column=5 )

#ADD ENTRY


button3=Button(window,text="Add Entry", command=add_entry, height=1,width=15 )
button3.grid(row=6,column=5 )



#UPDATE SELECTED
button4=Button(window, text="Update Selected", height=1,width=15 )
button4.grid(row=7,column=5 )
#DELETE SELECTED
button5=Button(window,text="Delete Selected", height=1,width=15)
button5.grid(row=8,column=5 )
#CLOSE PROGRAM
button6=Button(window,text="Close Program", height=1,width=15)
button6.grid(row=9,column=5 )





#CAPTURE USER INPUT
entry1_value=StringVar()
#USER INPUT
entry1=Entry(window, textvariable=entry1_value)
entry1.grid(row=0,column=1)


#LIST OF LIBRARY ENTRIES
library_books=Text(window, height=20,width=60, padx=(10), pady=10)
library_books.grid(row=5,column=1, padx=(80))






window.mainloop()

