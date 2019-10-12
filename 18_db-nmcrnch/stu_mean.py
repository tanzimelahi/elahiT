import csv
import sqlite3
DB_FILE="discobandit.db"
db=sqlite3.connect(DB_FILE)
c=db.cursor()
command="SELECT students.id FROM students"
c.execute(command)
student_id=c.fetchall()
command="CREATE TABLE if not EXISTS stu_avg(name TEXT,avg REAL, ID INTEGER)"
c.execute(command)
for roll in student_id:
    command='SELECT mark FROM courses WHERE courses.id=\"{}\"'
    c.execute(command.format(roll[0]))
    mark_id_list=c.fetchall()
    command='SELECT name FROM students WHERE students.id=\"{}\"'
    c.execute(command.format(roll[0]))
    name_id_list=c.fetchall()
    command='INSERT into stu_avg VALUES(\"{}\",\"{}\",\"{}\")'
    avg=0
    for num in mark_id_list:
        avg+=num[0]
    avg=avg/len(mark_id_list)
    c.execute(command.format(name_id_list[0][0],avg,roll[0]))
    #print (mark_id_list)
    #print(avg)
    #print(name_id_list)
    #print(roll)
command="INSERT into courses VALUES(\"{}\",\"{}\",\"{}\")"
c.execute(command.format("ap computer science",100,10))
c.execute(command.format("ap chemisty",100,1))
c.execute(command.format("ap calculus bc",100,2))
c.execute(command.format("multivariable calculus",100,2))
c.execute(command.format("complex calculus",100,3))
db.commit()
db.close()
