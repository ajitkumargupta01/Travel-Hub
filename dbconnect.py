import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="Username",  #Enter MySQL username
        password="Password", #Enter password 
        database="irctc"     #Create a database their name is irctc
    )