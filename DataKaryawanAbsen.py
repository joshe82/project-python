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


# FUNGSI
def opendb ():
    # FISRT TOP LEVEL KONEKSI DATA BASE
    global top
    top = Toplevel()
    top.title("Koneksi Database")
    top.geometry("500x400")
    top.configure(bg="darkgrey")
    
    label1=Label(top,bg="darkgrey", text="Pilih database :",fg="black", font="arial 18 bold")
    label1.place(x=10, y= 20)
    
    main_top=Frame(top)
    main_top.place(x=30,y=50)
    tabel = ttk.Treeview(main_top)
    verscrlbar = ttk.Scrollbar(top,orient ="vertical", command = tabel.yview)# scrollbar
    verscrlbar.pack(side ='right', fill ='x')
     # Configuring treeview
    tabel.configure(xscrollcommand = verscrlbar.set)
    tabel.pack()
    # Button TOP LEVEL
    button_buatdb=Button(top,text="Buat     Database",bg="Blue",fg="white",width=20,command=showCreatedb )
    button_buatdb.place(x=300, y=50)
    
    
           

def showCreatedb ():
    kotak = Frame(top,width=200, height=200, bg='green')
    kotak.place(x=275, y=100)
    
    labelNama_db=Label(kotak, text='Masukkan Nama Database', fg='white', bg='green')
    labelNama_db.place(x=10, y=20)
    inputNama = Entry(kotak,)
    inputNama.place(x=10, y=50)
    
    
    

# Button Main Frame
button_pilihdb=Button(app,text="Pilih Database", bg="Blue",fg="white",width=20,command=opendb )
button_pilihdb.place(x=30, y=20)






# END TOP LEVEL KONEKSI DATABASE















# First myFrame1
# Membuat function my_frame1
# set data base name 

def createdb() :
    mycursor = mydb.cursor()
    db=("CREATE DATABASE")
    mycursor.execute(db)
    print("Database baru berhasil dibuat")



    
    
    

def showlist_db():
    mycursor =mydb.cursor()
    db =("show databases")
    mycursor.execute(db)
    for (db) in cursor :
        print (db)
# End myFrame 1

app.mainloop()
