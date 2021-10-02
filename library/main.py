import sql

print('\nwelcome to eigen bookstore\n1.insert new record\n2.buy a book')

ch=int(input('\nenter the choice:'))
password='Jefjoseph@1209'
psw=input('\nenter the password:')

if psw==password:

	print('\nverifyiying......')
	if ch==1:

		tit=input('\nenter title of the book:')
		aut=input('\nenter the name of the author:')
		prc=int(input('\nenter the price of the book:'))
		sql.query(ch,tit,aut,prc)

	elif ch==2:

		
		tit=input('\nenter title of the book:')
		cop=float (input('\nenter the number of copies:'))
		price=sql.query(ch,tit)
		totalprice=price*cop
		print('total price is {} Rupees'.format(totalprice))

	else:
		print('\ninvalid choice')

else:
	print('\nincorrect password')


