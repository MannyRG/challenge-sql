import sqlite3

Sqldata= sqlite3.connect("db.sqlite3")

c = Sqldata.cursor()


c.execute("""SELECT school_id, ROUND(student_complete/total_students, 2) AS percentage FROM (SELECT school_id, student_complete, total_students FROM (SELECT school_id AS school_ids, COUNT(student_id) AS student_complete FROM (SELECT school_id, student_id, status FROM submission GROUP BY student_id) WHERE status="COMPLETED" GROUP BY school_id) LEFT JOIN (SELECT school_id, COUNT(student_id) AS total_students FROM (SELECT school_id, student_id, status FROM submission GROUP BY student_id) GROUP BY school_id) ON school_ids = school_id) """)




result = c.fetchall()
print(result)
