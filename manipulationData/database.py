import sqlite3 as sql

# Database functions
def addExtension(name, extension):
	nameCopy = name[:].replace('.', ' .').split()
	lenNameCopy = len(nameCopy)
	if lenNameCopy < 2 or nameCopy[lenNameCopy - 1] != extension:
		name += extension
	return name


def loadDatabase(name):
	nameDb = addExtension(name, '.db')
	db = sql.connect(nameDb)
	return db


class Database:
	def __init__(self, name):
		self.name = name
		self.database = loadDatabase(name)
		self.console = self.database.cursor()
		self.console.execute("CREATE TABLE IF NOT EXISTS tbl_people (id integer PRIMARY KEY AUTOINCREMENT, name text, date_birth text, gender text, marital_status text)")
		self.save()

	def insertInto(self, name, dateOfBirth, gender, maritalStatus):
		data = (name, dateOfBirth, gender, maritalStatus)
		self.console.execute("INSERT INTO tbl_people (name, date_birth, gender, marital_status) VALUES (?,?,?,?)", data)
		self.save()

	def select(self, command=None):
		if command == None:
			self.console.execute("SELECT * FROM tbl_people")
		else:
			try:
				self.console.execute(command)
			except:
				return self.select()
		return self.console.fetchall()

	def save(self):
		self.database.commit()

	def close(self):
		self.database.close()
