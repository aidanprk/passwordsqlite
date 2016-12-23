import sqlite3

#Functions
def new_user(name, password):
	#creates a new user under table: users

	conn = sqlite3.connect('userdata.dp')
	c = conn.cursor()

	c.execute('select max(id) from users;')
	id = c.fetchone()[0]

	if id == None:
		u_id = 1
	else:
		u_id = id + 1

	n = name
	p = password

	c.execute('''

		insert into users(id, name, password)
			values(?,?,?);

		''', (u_id, n, p))
	conn.commit()
	conn.close()
def qUsers():
	#quick-Users function prints all from table: users

	conn = sqlite3.connect('userdata.dp')
	c = conn.cursor()

	c.execute('select * from users;')
	print(c.fetchall())



	conn.close()
