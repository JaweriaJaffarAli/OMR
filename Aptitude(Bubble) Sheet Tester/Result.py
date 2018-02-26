import sqlite3 as lite
from sqlite3 import Error
import string

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    global conn
    try:
        conn = lite.connect("checker.db")
        c = conn.cursor()
        print(lite.version)
    except Error as e:
        print(e)
    finally:
        print("Connected")
        return (c, conn)


def close_connection(c):
    c.close()
    pass


# query = "CREATE TABLE result ("\
#         "Roll_no INT (100, 100) PRIMARY KEY"\
#         "                       UNIQUE"\
#         "                       NOT NULL,"\
#         "marks   INT (100, 100)"\
#         ");"


def login_check(username, password):
    pass_verf = None
    c, conn = create_connection("checker.db")

    query = """SELECT password FROM USER WHERE username = '{y}'""".format(y=username)
    c.execute(query)
    pass_verf = c.fetchone()
    if pass_verf == None:
        print('Invalid username or password')
        return 0
    else:
        pass_verf = pass_verf[0]
        if pass_verf == password:
            # login successful
            print('succesful')
            close_connection(c)
            return 1
        # login failed


# query = "INSERT INTO result(Roll_no, marks) VALUES ({x}, {y})".format(x = Roll_no, y = marks)

def register(username, password):
    c, conn = create_connection("checker.db")
    query = """SELECT * FROM USER WHERE username = '{y}'""".format(y=username)
    c.execute(query)
    conn.commit()
    result = c.fetchall()
    print(result)
    if len(result) == 0:
        query = '''INSERT INTO  USER (Username, Password) VALUES('{x}', '{y}')'''.format(x=username, y=password)
        c.execute(query)
        conn.commit()
        close_connection(c)
        return
    print('username already exist')


def register_select():
    c, conn = create_connection('checker.db')
    query = "SELECT * FROM USER"
    c.execute(query)
    print(c.fetchall())
    pass


def result(roll_id, marks):
    c, conn = create_connection("checkers.db")
    query = """SELECT * FROM RESULT WHERE RollNo = '{y}'""".format(y=roll_id)
    c.execute(query)
    conn.commit()
    result = c.fetchall()
    print(result)
    if len(result) == 0:
        query = '''INSERT INTO  RESULT (RollNo, Marks) VALUES({x}, {y})'''.format(x=roll_id, y=marks)
        c.execute(query)
        conn.commit()
        close_connection(c)
    return


def view_result():
    c, conn = create_connection("checkers.db")
    query = '''SELECT * FROM  RESULT'''
    c.execute(query)
    print(c.fetchall())
    pass

if __name__ == '__main__':
    login_check(3807931 , 'jia123')