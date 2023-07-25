#___________________МОДУЛЬ_8__УРОВЕНЬ1_НАЧАЛО____________________
import sqlite3
from datetime import datetime, time

conn = sqlite3.connect('StudyDB.sqlite')

cursor = conn.cursor()

# Создание таблицы "Students"
cursor.execute('''
	CREATE TABLE IF NOT EXISTS Students (
		id INTEGER PRIMARY KEY,
		name Varchar(32),
		surname Varchar(32),
		age INTEGER,
		city Varchar(32)
	)
''')

# Создание таблицы "Courses"
cursor.execute('''
	CREATE TABLE IF NOT EXISTS Courses (
		id INTEGER PRIMARY KEY,
		name Varchar(32),
		time_start DATE,
		time_end DATE
	)
''')

# Создание таблицы "Student_courses"
cursor.execute('''
	CREATE TABLE IF NOT EXISTS Student_courses (
		student_id INTEGER,
		course_id INTEGER,
		FOREIGN KEY (student_id) REFERENCES Students (id),
		FOREIGN KEY (course_id) REFERENCES Courses (id)
	)
''')
#___________________МОДУЛЬ_8__УРОВЕНЬ1_КОНЕЦ____________________

#___________________МОДУЛЬ_8__УРОВЕНЬ2_НАЧАЛО____________________
# Заполнение таблиц, если пустые
cursor.execute('SELECT COUNT(*) FROM Students')
result = cursor.fetchone()[0]

if result == 0:
	students_data = [
	(1, 'Max', 'Brooks', 24, 'Spb'),
	(2, 'John', 'Stones', 15, 'Spb'),
	(3, 'Andy', 'Wings', 45, 'Manhester'),
	(4, 'Kate', 'Brooks', 34, 'Spb')
	]
	cursor.executemany('INSERT INTO Students VALUES (?, ?, ?, ?, ?)', students_data)

cursor.execute('SELECT COUNT(*) FROM Courses')
result = cursor.fetchone()[0]

if result == 0:
	courses_data = [
	(1, 'Python', '21.07.21', '21.08.21'),
	(2, 'java', '13.07.21', '16.08.21'),
	]
	cursor.executemany('INSERT INTO Courses VALUES (?, ?, ?, ?)', courses_data)

cursor.execute('SELECT COUNT(*) FROM Student_courses')
result = cursor.fetchone()[0]

if result == 0:
	student_courses_data = [
	(1, 1),
	(2, 1),
	(3, 1),
	(4, 2)
	]
	cursor.executemany('INSERT INTO Student_courses VALUES (?, ?)', student_courses_data)

students_over_30 = cursor.execute("SELECT name, surname FROM Students WHERE age > 30")
print('\nСтуденты старше 30 лет:')
for student1 in students_over_30:
	for student in student1:
		print(student, end=' ')
	print()

students_python_course = cursor.execute('''
	SELECT Students.name, Students.surname
	FROM Students
	INNER JOIN Student_courses ON Students.id = Student_courses.student_id
	INNER JOIN Courses ON Student_courses.course_id = Courses.id
	WHERE Courses.name = 'Python'
''')
print(f'\nВсе студенты, которые проходят курс по Python:')
for student1 in students_python_course:
	for student in student1:
		print(student, end=' ')
	print()

students_python_spb = cursor.execute('''
	SELECT Students.name, Students.surname
	FROM Students
	INNER JOIN Student_courses ON Students.id = Student_courses.student_id
	INNER JOIN Courses ON Student_courses.course_id = Courses.id
	WHERE Courses.name = 'Python' AND Students.city = 'Spb'
''')
print(f'\nВсе студенты, которые проходят курс по python и из Spb:')
for student1 in students_python_spb:
	for student in student1:
		print(student, end=' ')
	print()

conn.commit()
conn.close()
#___________________МОДУЛЬ_8__УРОВЕНЬ2_КОНЕЦ____________________


