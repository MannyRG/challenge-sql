import sqlite3

Sqldata= sqlite3.connect("db.sqlite3")

c = Sqldata.cursor()

c.execute("SELECT course.name, ROUND(AVG(submission.grade), 2) AS average FROM course Left JOIN submission ON course.id = submission.course_id GROUP BY submission.course_id")



result = c.fetchall()
print(result)




