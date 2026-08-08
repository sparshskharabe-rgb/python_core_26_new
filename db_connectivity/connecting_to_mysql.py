import mysql.connector
from mysql.connector import Error

def showDatabases():
    print("Inside showDatabases")
    try:
        # Connection code
        # Step 1 : Get the connection object
        con = mysql.connector.connect(host='localhost', database='proj_activity', user='root', password='root')
        print("Successfully connected to DB.")

        # Step 2 : from connection object get the cursor
        cursor = con.cursor()

        # Step 3: Execute query using cursor object
        cursor.execute("show databases")

        for database_name in cursor:
            print(database_name)

        print("Fetch Complete")

    except Error as e:
        print("Exception while connecting - ", e)

    finally:
        # close the connection
        if cursor:
            cursor.close()
        if con:
            con.close()



def createNewDatabase():
    print("Creating a new database.......")
    try:
        # Connection code
        # Step 1 : Get the connection object
        con = mysql.connector.connect(host='localhost', database='proj_activity', user='root', password='root')
        print("Successfully connected to DB.")

        # Step 2 : from connection object get the cursor
        cursor = con.cursor()

        # Step 3: Execute query using cursor object
        cursor.execute("create database myowndb")

        print("Database creation complete")

    except Error as e:
        print("Exception while connecting - ", e)

    finally:
        # close the connection
        if cursor:
            cursor.close()
        if con:
            con.close()


def createTableInDatabase():
    print("Creating a new table.......")
    try:
        # Connection code
        # Step 1 : Get the connection object
        con = mysql.connector.connect(host='localhost', database='proj_activity', user='root', password='root')
        print("Successfully connected to DB.")

        # Step 2 : from connection object get the cursor
        cursor = con.cursor()

        # Step 3: Execute query using cursor object
        cursor.execute("create table login (userid varchar(20), password varchar(15), isadmin tinyint(1))")

        print("Table creation complete")

    except Error as e:
        print("Exception while connecting - ", e)

    finally:
        # close the connection
        if cursor:
            cursor.close()
        if con:
            con.close()

def insertDataInTable():
    print("Inserting data in table.......")
    try:
        # Connection code
        # Step 1 : Get the connection object
        con = mysql.connector.connect(host='localhost', database='proj_activity', user='root', password='root')
        print("Successfully connected to DB.")

        # Step 2 : from connection object get the cursor
        cursor = con.cursor()

        # Step 3: Execute query using cursor object
        cursor.execute("insert into login values('admin','pass', 1)")

        # commit the inserted data
        con.commit()

        print("Record Inserted Successfully")

    except Error as e:
        print("Exception while connecting - ", e)

    finally:
        # close the connection
        if cursor:
            cursor.close()
        if con:
            con.close()


def fetchAllDataFromTable():
    print("Fetching data from table.......")
    try:
        # Connection code
        # Step 1 : Get the connection object
        con = mysql.connector.connect(host='localhost', database='proj_activity', user='root', password='root')
        print("Successfully connected to DB.")

        # Step 2 : from connection object get the cursor
        cursor = con.cursor()

        # Step 3: Execute query using cursor object
        cursor.execute("select * from login")

        resultset = cursor.fetchall() # returns list of tuples, to fetch all the records coming from DB

        print(resultset)

        for record in resultset:
            print("Userid : {}, Password : {}, IsAdmin : {}".format(record[0], record[1], record[2]))

        print("Record Fetched Successfully")

    except Error as e:
        print("Exception while connecting - ", e)

    finally:
        # close the connection
        if cursor:
            cursor.close()
        if con:
            con.close()

def fetchOneDataFromTable():
    print("Fetching data from table.......")
    try:
        # Connection code
        # Step 1 : Get the connection object
        con = mysql.connector.connect(host='localhost', database='proj_activity', user='root', password='root')
        print("Successfully connected to DB.")

        # Step 2 : from connection object get the cursor
        cursor = con.cursor()

        # Step 3: Execute query using cursor object
        cursor.execute("select * from login where userid = 'user'")

        resultset = cursor.fetchone() # to fetch all the records coming from DB, tuple

        print(resultset)

        print("Userid : {}, Password : {}, IsAdmin : {}".format(resultset[0], resultset[1], resultset[2]))

        print("Record Fetched Successfully")

    except Error as e:
        print("Exception while connecting - ", e)

    finally:
        # close the connection
        if cursor:
            cursor.close()
        if con:
            con.close()




if __name__ == '__main__':
    print("Starting main")
    #showDatabases()
    #createNewDatabase()
    # createTableInDatabase()
    #insertDataInTable()
    #fetchAllDataFromTable()
    fetchOneDataFromTable()