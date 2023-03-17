import mysql.connector


mydb=mysql.connector.connect(
    host = "localhost",
    user ="root",
    passwd = ""
)

# set data base name ...
# namadatabase =input("masukan Nama Db :")


# Fungsi untuk CREATE DATABASE
def createdb() :
    mycursor = mydb.cursor()
    db=("CREATE DATABASE {}".format(namadatabase))
    mycursor.execute(db)
    print("Database baru berhasil dibuat")




# Fungsi untuk DROP DATABASE
def dropdb():
    mycursor = mydb.cursor()
    db = "DROP DATABASE {}".format(namadatabase)
    mycursor.execute(db)
    print("Database {} berhasil dihapus".format(namadatabase))

def listdb():
    mycursor=mydb.cursor()
    mycursor.execute("SHOW DATABASES") # execute the SHOW DATABASES query
    databases= mycursor.fetchall() # get the list of databases 
     
    for db in databases:
        print(db)
        
        
listdb()