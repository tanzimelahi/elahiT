#Tanzim Elahi and his Duck
#SoftDev
#skeleton :: SQLITE3 BASICS
#Oct 2019

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

# < < < INSERT YOUR POPULATE-THE-DB CODE HERE > > >
command="CREATE TABLE IF NOT EXISTS courses(code TEXT,mark INTEGER,id INTEGER)"
c.execute(command);
with open('courses.csv', newline='') as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
          rcommand="INSERT INTO courses VALUES(\"{}\",\"{}\",\"{}\");".format(row["code"],row["mark"],row["id"])
          c.execute(rcommand);

command="CREATE TABLE IF NOT EXISTS students(name TEXT,age INTEGER,id INTEGER)"
c.execute(command);
with open('students.csv', newline='') as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
          rcommand="INSERT INTO courses VALUES(\"{}\",\"{}\",\"{}\");".format(row["name"],row["age"],row["id"])
          c.execute(rcommand);
#==========================================================

db.commit() #save changes
db.close()  #close database
