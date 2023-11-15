import sqlite3

db_connection = sqlite3.connect('student_information.db')
cursor = db_connection.cursor()

cursor.execute('''CREATE TABLE student_information (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    roll_no INTEGER,
                    institution TEXT
                )''')

cursor.execute("INSERT INTO student_information (name, roll_no, institution) VALUES (?, ?, ?)", ("ram", 2310628, "Anna university"))
db_connection.commit()
db_connection.close()