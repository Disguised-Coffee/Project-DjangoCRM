# TO make a database

import mysql.connector

dataBase = mysql.connector.connect(
    
    )

#Prepare a cursor obj
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE tryhardstudios")

print("All Done!")