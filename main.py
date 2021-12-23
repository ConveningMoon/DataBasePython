import sqlite3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

con = sqlite3.connect("works.sqlite")
cursor = con.cursor()

cursor.execute("CREATE TABLE Genders("
               "ID_gender INTEGER PRIMARY KEY AUTOINCREMENT,"
               "gender TEXT"
               ")")
con.commit()

cursor.execute("CREATE TABLE Education("
               "ID_education INTEGER PRIMARY KEY AUTOINCREMENT,"
               "educationType TEXT"
               ")")
con.commit()

cursor.execute("CREATE TABLE JobTitle("
               "ID_jobtitle INTEGER PRIMARY KEY AUTOINCREMENT,"
               "jobTitle TEXT"
               ")")
con.commit()

cursor.execute("CREATE TABLE Qualification("
               "ID_qualification INTEGER PRIMARY KEY AUTOINCREMENT,"
               "qualification TEXT"
               ")")
con.commit()

cursor.execute(""" INSERT INTO Genders (gender)
                    VALUES 
                        ('Женщина'),
                        ('Мужчина')
                """)
con.commit()

cursor.execute(""" INSERT INTO Education (educationType)
                    VALUES 
                        ('Высшее'),
                        ('Среднее')
                """)
con.commit()

cursor.execute(""" INSERT INTO JobTitle (jobTitle)
                    VALUES 
                        (''),
                        ('Мужчина')
                """)
con.commit()

cursor.execute(""" INSERT INTO Qualification (qualification)
                    VALUES 
                        ('Инженер'),
                        ('Повар'),
                        ('Магистр')                
                """)
con.commit()
