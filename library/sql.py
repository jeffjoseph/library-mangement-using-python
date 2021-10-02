
import sqlite3



def query(a,b,c=None,d=None):


	try:
		con=sqlite3.connect('lib.db')
		cur=con.cursor()
		cur.execute("""SELECT name FROM sqlite_master WHERE type='table'
	  AND name='book'""")
		
		#checking if there is one table
		if cur.fetchall()==[]:
			cur.execute('CREATE TABLE book(title text,author text,price real)')
		
		#inserting new record
		elif a==1:
			sql="""INSERT INTO book (title,author,price) VALUES (?,?,?)"""
			cur.execute(sql,(b,c,d))
			con.commit()
			print("successfully inserted")

		#retrieve data
		elif a==2:
			sql="""SELECT price FROM book WHERE title=?"""
			cur.execute(sql,(b,))
			tup=cur.fetchone()
			return float(tup[0])
			 

			

	except Exception as e:

		print(e)


	finally:

		print('database closed')
		con.close()





		







