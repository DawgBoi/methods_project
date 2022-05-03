import mysql.connector
import sys

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="project"
    )

    print("Successful connection.")

except:
    print("Failed connection.")

    sys.exit()

cursor = connection.cursor()

class orderHist:
    def __init__(self,UserID):
        self.UserID = UserID

    def getUserID():
        return UserID

    def getMovieID():
        query = "SELECT MovieID FROM orderhistory WHERE UserID=%d"
        data = UserID
        cursor.execute(query,data)
        result = cursor.fetchall()
        return result

    def getTitle():
        query = "SELECT Title FROM orderhistory WHERE UserID=%d"
        data = UserID
        cursor.execute(query,data)
        result = cursor.fetchall()
        return result

    def getAmount():
        query = "SELECT amount FROM orderhistory WHERE UserID=%d"
        data = UserID
        cursor.execute(query,data)
        result = cursor.fetchall()
        return result

    def getTotal():
        query = "SELECT total FROM orderhistory WHERE UserID=%d"
        data = UserID
        cursor.execute(query,data)
        result = cursor.fetchall()
        return result

    def getDateOrdered():
        query = "SELECT dateOrdered FROM orderhistory WHERE UserID=%d"
        data = UserID
        cursor.execute(query,data)
        result = cursor.fetchall()
        return result

    def viewOrderHistory(self):
        query = "SELECT * FROM orderhistory WHERE UserID=%d"
        data = UserID
        cursor.execute(query,data)
        result = cursor.fetchall()
        for x in result:
            print("ID: ", x[0], "\nMovie ID: ", x[1], "\nTitle: ", x[2], "\nAmount: ", x[3], "\nTotal: ", x[4], "\nDate Ordered: ", x[5])
        return

    def pushOrderHistory(MovieID,Title,amount,total,dateOrdered):
        query = "INSERT INTO `orderhistory` (`UserID`, `MovieID`, `Title`, `amount`, `total`, `dateOrdered`) VALUES (%d,%d,%s,%d,%d,%s)"
        data = (UserID,MovieID,Title,amount,total,dateOrdered)
        cursor.execute(query,data)
        print("Order added to history")
        return 