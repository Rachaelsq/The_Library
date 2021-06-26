import sqlite3

def connect():
  conn=sqlite3.connect("books.db")
  cur=conn.cursor()
  cur.execute("CREATE TABLE IF NOT EXISTS book(id INTERGER PRIMARY KEY, title text, author text, year interget, isbn interger)")
  conn.commit()
  conn.cose()

  def connect():
  conn=sqlite3.connect("books.db")
  cur=conn.cursor()
  cur.execute("CREATE TABLE IF NOT EXISTS book(id INTERGER PRIMARY KEY, title text, author text, year interget, isbn interger)")
  conn.commit()
  conn.cose()

  def connect():
  conn=sqlite3.connect("books.db")
  cur=conn.cursor()
  cur.execute("CREATE TABLE IF NOT EXISTS book(id INTERGER PRIMARY KEY, title text, author text, year interget, isbn interger)")
  conn.commit()
  conn.cose()




  connect()