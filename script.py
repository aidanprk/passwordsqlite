import sqlite3
import random

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
def generate_password():
	#generates a random numeric password
	length = 8
	password = []
	for x in range(1,9):
		password.append(str(random.randint(1,9)))

	pw = ''.join(password)
	return(pw)

names = ['Sophia',	'Jackson','Emma', 'Aiden', 'Olivia', 'Lucas',
		'Ava', 'Liam', 'Mia', 'Noah', 'Isabella', 'Ethan', 'Riley',
		 'Mason', 'Aria', 'Caden', 'Zoe', 'Oliver', 'Charlotte',
		 'Elijah', 'Lily', 'Grayson', 'Layla', 'Jacob', 'Amelia',
		 'Michael', 'Emily', 'Benjamin', 'Madelyn', 'Carter', 
		 'James', 'Adalyn',	'Jayden', 'Madison', 'Logan', 'Chloe',
		 'Alexander', 'Harper',	'Caleb', 'Abigail',	'Ryan','Aaliyah',
		 'Luke', 'Avery', 'Daniel', 'Evelyn', 'Jack', 'Kaylee',	
		 'William', 'Ella', 'Owen', 'Ellie', 'Gabriel', 'Scarlett',	
		 'Matthew', 'Arianna', 'Connor', 'Hailey', 'Jayce', 'Nora',	
		 'Isaac']

def scramble_password(id):

	censor = ['!','@','#','$','%','^','&','*','(']
	new_password = []
	conn = sqlite3.connect('userdata.dp')
	c = conn.cursor()

	u_id = (id,)

	c.execute('select password from users where id = ?', u_id)
	password = c.fetchall()[0]

	random.shuffle(censor)
	for letter in str(password[0]):
		new_password.append(letter)
		new_password.append(censor[random.randint(0,8)])

	random.shuffle(new_password)
	pw = ''.join(new_password)
	spw = (pw,)

	c.execute('''

		update users,
		set password = ?
		where id = ?;

		''', (spw, u_id))



	



scramble_password(4)







