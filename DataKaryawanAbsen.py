import tkinter as tk
from tkinter import messagebox
from tkinter import *
from  tkinter import ttk
import mysql.connector

# koneksi database
mydb=mysql.connector.connect(
    host = "localhost",
    user ="root",
    passwd = ""
)

# Main Frame Windows Aplikasi Data Karyawan  
app =Tk()
app.title("Aplikasi Data Karyawan")
app.geometry("900x900")

namedb_controller=StringVar()

# FUNGSI
def opendb ():
    # FISRT TOP LEVEL KONEKSI DATA BASE
    global top,tabel
    top = Toplevel()
    top.title("Koneksi Database")
    top.geometry("500x400")
    top.configure(bg="darkgrey")
    
    label1=Label(top,bg="darkgrey", text="Pilih database :",fg="black", font="arial 18 bold")
    label1.place(x=10, y= 20)
    
    listButton=Button(top,text="List DB",bg="green",fg="white",width=10,command=listdb)
    listButton.place(x=350,y=20)
    
    main_top=Frame(top)
    main_top.place(x=30,y=50)
    
    # Membuat Tabel 
    tabel = ttk.Treeview(main_top, columns=("name"), show="headings")
    tabel.heading("name", text="Database Name")
    tabel.pack()
    
    
    # Button TOP LEVEL
    button_buatdb=Button(top,text="Buat Database",bg="Blue",fg="white",width=20,command=showCreatedb )
    button_buatdb.place(x=300, y=50)
    
 
def showCreatedb ():
    # Frame Form Database
    kotak = Frame(top,width=200, height=200, bg='grey')
    kotak.place(x=275, y=100)
    # Label Frame Database
    labelNama_db=Label(kotak, text='Masukkan Nama Database', fg='white', bg='grey', font="Arial 10 bold")
    labelNama_db.place(x=10, y=20)
    inputNama = Entry(kotak,textvariable=namedb_controller)
    inputNama.place(x=10, y=50)
    # Button on Frame form database
    submit=Button(kotak, width=10,text="Submit", bg="red", fg="white", font="Arial 10 bold",command=createdb)
    submit.place(x=20, y=100)
    
# set data base name 

def createdb() :
    mycursor = mydb.cursor()
    namedb=namedb_controller.get()
    db=("CREATE DATABASE {}".format(namedb))
    mycursor.execute(db)
    pesan="Database berhasil dibuat"
    messagebox.showinfo("info",message=pesan)

    
def listdb():
    global mydb, tabel
    tabel.delete(*tabel.get_children())
    mycursor=mydb.cursor()
    mycursor.execute("SHOW DATABASES") # execute the SHOW DATABASES query
    databases= mycursor.fetchall() # get the list of databases 
     
    for db in databases:
        print(db)
        tabel.insert(parent="",index="end", text="",value =(db[0]))
        
        

    
    

# Button Main Frame
button_pilihdb=Button(app,text="Pilih Database", bg="Blue",fg="white",width=20,command=opendb)
button_pilihdb.place(x=30, y=20)






# END TOP LEVEL KONEKSI DATABASE



















    
    
    

def showlist_db():
    mycursor =mydb.cursor()
    db =("show databases")
    mycursor.execute(db)
    for (db) in cursor :
        print (db)
# End myFrame 1

app.mainloop()
