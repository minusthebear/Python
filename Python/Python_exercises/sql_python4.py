import sqlite3

peopleValues = (('Jean-Baptiste Zorg', 'Human', 122),
('Korben Dallas', 'Meat Popsicle', 100),
('Ak\'not', 'Mangalore', -5))

connection = sqlite3.connect(':memory:')

c = connection.cursor()

c.executescript("""DROP TABLE IF EXISTS Roster; CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT);""")
c.executemany("INSERT INTO Roster VALUES(?, ?, ?)", peopleValues)

c.execute("SELECT * FROM Roster")
while True:
	row = c.fetchone()
	if row is None:
		break
	print row

c.execute("UPDATE Roster SET Species=? WHERE Name=? AND IQ=?",('Human', 'Korben Dallas', 100))

c.execute("SELECT Name, IQ FROM Roster WHERE Species='Human'")
while True:
	row = c.fetchone()
	if row is None:
		break
	print row
