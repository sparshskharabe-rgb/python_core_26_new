import mysql.connector
from mysql.connector import Error
class LoginDAO:
    def getLoginDeatilsFromDB(username, password):
        print("Make a call to DB to ftech the details of the user for provided username and password combination and return it.")
        ## Code for DB call 
        print(username, password)

        try: 

            query = "select userid, password, isadmin from login where userid='" + username +"' and password='" + password + "'"
            print(query)
            # Step 1 - Get the connection object
            con = mysql.connector.connect(host='localhost', database='proj_activity', user='root', password='root')
            
            # Now execute the sqlquery 
            cursor = con.cursor() 
            cursor.execute(query) 

            resultset = cursor.fetchone() # tuple
            print(resultset)

            if resultset is None:
                return None
            
            return resultset
            
        except Error as e: 
            print("Exception Raised while connecting - ", e)  
        
        finally: 
            if cursor: 
                cursor.close() 
            if con: 
                con.close() 
                