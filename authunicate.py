from dbconnect import get_connection

def check_user(email, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, password))
    return cursor.fetchone()

def create_Table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            first_name VARCHAR(100),
            last_name VARCHAR(100),
            email VARCHAR(255) PRIMARY KEY,
            password VARCHAR(255),
            mob_num VARCHAR(15),
            gender VARCHAR(10),
            address TEXT,
            city VARCHAR(100),
            state VARCHAR(100),
            pin_code VARCHAR(10)
        )
    ''')

    conn.commit()
    conn.close()


def register_user(data):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s,%s)
    """, data)
    conn.commit()
    conn.close()

def get_user(email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
    user = cursor.fetchone()
    conn.close()
    return user

def create_train_Table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS trains (
            train_name varchar(20),
            train_no varchar(5) primary key,
            source varchar(25),
            destination varchar(25),
            departure varchar(7),
            arrival varchar(7),
            duration varchar(10),
            date varchar(25),
            class1 varchar(30),
            class2 varchar(35),
            class3 varchar(30),
            class4 varchar(35)
        )
    ''')
    conn.commit()
    conn.close()

def search_train(source, destination):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM trains WHERE source=%s AND destination=%s", (source, destination))
    return cursor.fetchone()

def create_Passenser_Table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS passengers (
            email varchar(30),
            pnr varchar(10),
            name varchar(20),
            source varchar(20),
            destination varchar(25),
            class varchar(40),
            seat varchar(20)
        )
    ''')
    conn.commit()
    conn.close()

def register_passengers(data):  
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO passengers VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, data)
    conn.commit()
    conn.close()


def get_passengers(email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM passengers WHERE email = %s", (email,))
    passengers = cursor.fetchall()
    cursor.execute("""
        SELECT COUNT(*) 
        FROM passengers 
        WHERE email = %s 
        GROUP BY email 
        HAVING COUNT(*) > 1
    """, (email,))
    conn.close()
    return passengers


def cancel_ticket(pnr):
    conn = get_connection()
    cursor = conn.cursor()
    ret=cursor.execute("delete from passengers where pnr=%s ",(pnr,))
    conn.commit()
    conn.close()


def update_details(first_name, last_name, password, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE users SET first_name = %s, last_name = %s, password = %s WHERE email = %s",
        (first_name, last_name, password, email)
    )
    conn.commit()  
    cursor.close()
    conn.close()
    return True