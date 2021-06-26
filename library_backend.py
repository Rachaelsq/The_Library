import sqlite3


#====================
#====BACK END
#====================

#STEP 1: CREATE (DATABASE
def connect():
  conn=sqlite3.connect("booksdatabase.db")
  cur=conn.cursor()
  cur.execute("CREATE TABLE IF NOT EXISTS booktable(id INTERGER PRIMARY KEY, title text, category text, author text, isbn interger)")
  conn.commit()
  conn.close()

#STEP 2: COMMIT CHANGES TO THE DATABASE/ ADD A BOOK ENTRY
def insert(title, category, author, isbn):
  conn=sqlite3.connect("booksdatabase.db")
  cur=conn.cursor()
  cur.execute("INSERT INTO booktable VALUES (id INTERGER PRIMARY KEY,?,?,?,?)",(title, category, author, isbn))
  conn.commit()
  conn.close()

#STEP 3: VIEW
def view():
  conn=sqlite3.connect("booksdatabase.db")
  cur=conn.cursor()
  cur.execute("SELECT * FROM booktable")
  rows=cur.fetchall()
  conn.close()
  return rows

#STEP 3: DELETE
""" def delete():
  conn=sqlite3.connect("booksdatabase.db")
  cur=conn.cursor()
  cur.execute("DELETE FROM book WHERE id=?",(id,))
  rows=cur.fetchall()
  conn.close()
  return rows
"""
#====================
#====SEARCH
#====================

def search(title="",category="",author="",isbn=""):
  conn=sqlite3.connect("booksdatabase.db")
  cur=conn.cursor()
  cur.execute("SELECT * FROM booktable WHERE title=? OR author=? OR category=? OR isbn=?", (title,category,author,isbn))
  rows=cur.fetchall()
  conn.close()
  return rows







#====================
#====RUN
#====================
connect()
insert("on the beach", "romance", "john doe", 5424546)
print(view())
print(search(author="john doe"))













