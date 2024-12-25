import MySQLdb

dataBase = MySQLdb.connect(
    host='localhost',
    user='root',
    passwd='123456789'
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE alpha")
print("All Done!")
