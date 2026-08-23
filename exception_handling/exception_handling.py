# Errors

# Errors are the problems in a problem that causes the program to terminate

# 1. Syntax Errors
# Missing Indentations, missing language definitions, missing command
# Compiler can detect it

# 2. Logical Errors (Exceptions)
# logical => Exception

# Def : Exception is an event that occurs during the execution of a program and disrupts the normal flow of execution.
# It happens at RUNTIME (runtime error) and terminates the execution of program, if not handled properly.

# Types
# Inbuilt : Exception => ZeroDivisionError, ValueError, IndexError, KeyError, MemoryError, NameError, RunTimeException
# Custom : created by user

# Exception Raised (Occur) => Exception Handling
# try...except => blocks are used handled the exception
# try => put the piece of code that could generate the exception
# except => logic to handle it or fallback logic
# finally => it executes irrespective of whether there is an exception or not.
#            Usage : cleaning of resources like closing the connection, file, cursor, sockets etc.
# else => called when there is no exception



# Combinations of try...except....else.....finally


try:
    pass
except:
    pass


try:
    pass
finally:
    pass

try:
    pass
except:
    pass
finally:
    pass


try:
    pass
except:
    pass
else:
    pass
finally:
    pass


try:
    pass
except:
    pass
else:
    pass





import mysql.connector
from mysql.connector import Error

def zerodivisionexception():
    num1, num2 = 10, 0
    result = num1/num2 # division operation, exception point
    print(result)


def zerodivisionexceptionhandled():
    num1, num2 = 10, 0
    try:
        result = num1 / num2  # division operation, exception point
        print(result)
    except Exception as e:
        print("Exception Raised", e)


def file_operation_handling():
    try:
        myfile = open("textfile.txt") # file might not exist in the directory, FileNotFoundError exception will be raised
        myfile.read()
        myfile.close() # File closed
        #10 / 0  # ZeroDivisionError
        #myfile.read() # Reading a closed file. Exception Raised, ValueError
    except FileNotFoundError as e: # Specific handling
        print("Exception while opening the file : ", e.strerror)
    except ValueError as e: # Specific handling
        print("File is closed. Please open it first : ", e)
    except ZeroDivisionError as e: # Specific handling
        print("Exception while divison", e)
    except Exception as e: # Generic handling. It should always placed at the end if we have multiple exception handling blocks
        print(e)
    else:
        print("Process completed without any issues")
    finally:
        print("Cleaning up the resources")
        if myfile:
            myfile.close()

def getLoginDeatilsFromDB():
    username = 'root'
    password = 'root'

    try:

        query = "select userid, password, isadmin from login where userid='" + username + "' and password='" + password + "'"
        print(query)
        # Step 1 - Get the connection object
        con = mysql.connector.connect(host='localhost', database='proj_activity', user='root', password='root')

        # Now execute the sqlquery
        cursor = con.cursor()
        cursor.execute(query)

        resultset = cursor.fetchone()  # tuple
        print(resultset)

    except Exception as e:
        print("Exception Raised while connecting - ", e)
    else:
        print("Process completed without any issues")
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()

if __name__ == '__main__':
    print("Exception Demo Begins...")
    #zerodivisionexception()
    #zerodivisionexceptionhandled()
    #file_operation_handling()
    getLoginDeatilsFromDB()
    print("End of exception Demo.")
