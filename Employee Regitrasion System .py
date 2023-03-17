import tkinter as tk
from tkinter import messagebox
from tkinter import *
from  tkinter import ttk
import mysql.connector

# koneksi database
def connection_db(database):
    mydb=mysql.connector.connect(
        host = "localhost",
        user ="root",
        passwd = "",
        database=database)
    return mydb  
        

app =Tk()
app.title("Sistem Registrasi Karyawan")
app.geometry("1080x720")
app.configure(bg="lightgrey")

namedb_controller=StringVar()
mydatabase_controller =StringVar()
idkryControl=StringVar()
namaControl=StringVar()
jabatanControl=StringVar()
alamatControl=StringVar()
teleponControl=StringVar()
databaseControl=StringVar()
searchControl=StringVar()

# FUNCTION ON MAIN-APP

def read():
    global mydb, tabel1
    tabel1.delete(*tabel1.get_children())
    try :
        text = databaselabel.cget("text")
    except NameError:
        messagebox.showerror("Error","Database Anda belum dipilih")
        return
    database = text
    mydb=connection_db(database)
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM employeetabel")
    results=cursor.fetchall()
    
    for data in results:
        print(data)
        tabel1.insert(parent="",index="end", text="", value=(data[0],data[1],data[2],data[3],data[4]))
        
def add() :
    global mydb
    try :
        text=databaselabel.cget("text")
    except NameError:
        messagebox.showerror("Error","Database Anda belum dipilih")
        return
    database=text    
        
    try :    
        mydb= connection_db(database)
        cursor = mydb.cursor()
        sql="INSERT INTO employeetabel(idkry,nama,jabatan,alamat,telepon) VALUES(%s,%s,%s,%s,%s)"
        data_baru=(idkryControl.get(),namaControl.get(),jabatanControl.get(),alamatControl.get(),teleponControl.get())
        cursor.execute(sql,data_baru)
        mydb.commit()
        messagebox.showinfo("Info", "Data Berhasil disimpan")
    except mysql.connector.Error as err:
        pesan = "Sorry..!{}".format(err)
        messagebox.showwarning("WARNING",message=pesan)
    read()
        
def update() :
    global mydb
    try :
        text=databaselabel.cget("text")
    except NameError:
        messagebox.showerror("Error","Database Anda belum dipilih")
        return
    database=text
    mydb= connection_db(database)
    
    if namaControl.get() != '' :
        cursor=mydb.cursor()
        sql ="UPDATE employeetabel SET nama=%s WHERE idkry=%s"
        dataUpdate= (namaControl.get(),idkryControl.get())
        cursor.execute(sql,dataUpdate)
    
    if jabatanControl.get() != '' :
        cursor=mydb.cursor()
        sql ="UPDATE employeetabel SET jabatan=%s WHERE idkry=%s"
        dataUpdate= (jabatanControl.get(),idkryControl.get())
        cursor.execute(sql,dataUpdate)
    
    if alamatControl.get() != '' :
        cursor=mydb.cursor()
        sql ="UPDATE employeetabel SET alamat=%s WHERE idkry=%s"
        dataUpdate= (alamatControl.get(),idkryControl.get())
        cursor.execute(sql,dataUpdate)
    
    if teleponControl.get() != '' :
        cursor=mydb.cursor()
        sql ="UPDATE employeetabel SET telepon=%s WHERE idkry=%s"
        dataUpdate= (teleponControl.get(),idkryControl.get())
        cursor.execute(sql,dataUpdate)
    mydb.commit()      
    messagebox.showinfo("INFO", "Data Berhasil di UPDATE")
    read()

def delete() :
    global mydb
    try :
        text=databaselabel.cget("text")
    except NameError:
        messagebox.showerror("Error","Database Anda belum dipilih")
        return
    
    confirm = messagebox.askyesno("Confirm Delete", "Apakah anda yakin menghapus data?")
    
    if confirm :
        database=text
        mydb= connection_db(database)
        cursor=mydb.cursor()
        textsearch=idkryControl.get()
        cursor.execute("DELETE FROM employeetabel  WHERE idkry = {}".format(textsearch))
        mydb.commit()
        messagebox.showinfo("INFO","Data Berhasil di HAPUS")
        read()
    
    

def search():
    global mydb
    try :
        text=databaselabel.cget("text")
    except NameError:
        messagebox.showerror("Error","Database Anda belum dipilih")
        return
    database=text
    mydb= connection_db(database)
    cursor=mydb.cursor()
    textsearch=searchControl.get()
    cursor.execute("SELECT * FROM employeetabel  WHERE idkry = {}".format(textsearch))
    result=cursor.fetchall()
    
    for data in result :
        print(data)
        idkryControl.set(data[0])
        namaControl.set(data[1])
        jabatanControl.set(data[2])
        alamatControl.set(data[3])
        teleponControl.set(data[4])
        

def reset () :
    searchControl.set('')
    idkryControl.set('')
    namaControl.set('')
    jabatanControl.set('')
    alamatControl.set('')
    teleponControl.set('')


# Main Frame Windows Aplikasi Data Karyawan 

tlabel=Label(app,text="Sistem Registrasi Karyawan", font= "Arial 16 bold", fg="black", bg = "lightgrey")
tlabel.place(x=300,y=20)

# Create Combo Box for Search

idkrylabel=Label(app, text="ID Karyawan",font="Arial 15",bg="lightgrey" )
namalabel=Label(app, text="Nama",font="Arial 15",bg="lightgrey" )
jabatanlabel=Label(app, text="Jabatan",font="Arial 15",bg="lightgrey" )
alamatlabel=Label(app, text="Alamat",font="Arial 15",bg="lightgrey" )
teleponlabel=Label(app, text="Telepon",font="Arial 15",bg="lightgrey" )

idkrylabel.place(x=20,y=150)
namalabel.place(x=20,y=200)
jabatanlabel.place(x=20,y=250)
alamatlabel.place(x=20,y=300)
teleponlabel.place(x=20,y=350)

searchentry=Entry(app, width=35, bd=5, font="Arial 15",foreground="grey",textvariable=searchControl)
idkryentry=Entry(app, width=55, bd=5, font="Arial 15",textvariable=idkryControl )
namaentry=Entry(app, width=55, bd=5, font="Arial 15",textvariable=namaControl )
jabatanentry=Entry(app, width=55, bd=5, font="Arial 15",textvariable=jabatanControl )
alamatentry=Entry(app, width=55, bd=5, font="Arial 15",textvariable=alamatControl )
teleponentry=Entry(app, width=55, bd=5, font="Arial 15",textvariable=teleponControl )

searchentry.place(x=150,y=100)
idkryentry.place(x=150,y=150)
namaentry.place(x=150,y=200)
jabatanentry.place(x=150,y=250)
alamatentry.place(x=150,y=300)
teleponentry.place(x=150,y=350)

# Command Later 
addBtn=Button(app,text="Add", padx=65,pady=25,width=10,bd=5,font="arial 15 ", bg="#84f894",command=add)
updateBtn=Button(app,text="Update", padx=65,pady=25,width=10,bd=5,font="arial 15 ", bg="#84E8F8", command=update)
deleteBtn=Button(app,text="Delete", padx=65,pady=25,width=10,bd=5,font="arial 15 ", bg="#FF9999",command=delete)
searchBtn=Button(app,text="Search ID", padx=20,pady=5,width=5,bd=5,font="arial 15 ", bg="#F4FE82",command=search)
resetBtn=Button(app,text="Reset", padx=65,pady=25,width=10,bd=5,font="arial 15 ", bg="#F398FF",command=reset)
refreshBtn=Button(app,text="Refresh", padx=65,pady=25,width=10,bd=5,font="arial 15 ", bg="darkgrey",command=read)

addBtn.place(x=800,y=100)
updateBtn.place(x=800,y=200)
deleteBtn.place(x=800,y=300)
searchBtn.place(x=600,y=85)
resetBtn.place(x=800,y=400)
refreshBtn.place(x=800,y=500)



# Tabel Utama
main_app = Frame(app,bg="green")
main_app.place(x=150, y=400)

tabel1 = ttk.Treeview(main_app)
verscrlbar = ttk.Scrollbar(app,
                           orient ="vertical",
                           command = tabel1.yview)# scrollbar
verscrlbar.pack(side ='right', fill ='x')
 
# Configuring treeview
tabel1.configure(xscrollcommand = verscrlbar.set)


tabel1['columns'] = ('idkry', 'nama', 'jabatan', 'alamat',"telepon")

tabel1.column("#0", width=2,  stretch=NO)
tabel1.column("idkry",anchor=CENTER, width=100)
tabel1.column("nama",anchor=CENTER,width=100)
tabel1.column("jabatan",anchor=CENTER,width=100)
tabel1.column("alamat",anchor=CENTER,width=100)
tabel1.column("telepon",anchor=CENTER,width=100)


tabel1.heading("#0",text="", anchor=CENTER,)
tabel1.heading("idkry",text="Id Karyawan",anchor=CENTER)
tabel1.heading("nama",text="Nama",anchor=CENTER)
tabel1.heading("jabatan",text="Jabatan",anchor=CENTER)
tabel1.heading("alamat",text="Alamat",anchor=CENTER)
tabel1.heading("telepon",text="Telepon",anchor=CENTER)

tabel1.pack()


# FUNCTION ON TOP LEVEL
def opendb ():
    # FISRT-- Top level Database 
    global top,tabel
    top = Toplevel()
    top.title("Koneksi Database")
    top.geometry("350x400")
    top.configure(bg="darkgrey")
    
    label1=Label(top,bg="darkgrey", text="DATABASE",fg="black", font="arial 18 bold")
    label1.place(x=100, y= 20)
    
    # Membuat listbox 
    main_top=Frame(top)
    main_top.place(x=30,y=130)
    tabel = ttk.Treeview(main_top, columns=("name"), show="headings",)
    tabel.heading("name", text="Database Name")
    tabel.pack()
    
    # Style selection item
    style = ttk.Style()
    style.map("Treeview", foreground=[('selected', 'white')], background=[('selected', 'green')])


        
    # Button TOP LEVEL
    button_createdb=Button(top,text="Create",bg="Blue",fg="white",width=10,command=showCreatedb )
    button_createdb.place(x=250, y=100)
    button_list=Button(top,text="List",bg="green",fg="white",width=10,command=listdb)
    button_list.place(x=250,y=130)    
    button_selectdb=Button(top,text="Select DB",bg="orange",fg="white",width=10,command=on_database_selection,)
    button_selectdb.place(x=250, y=160)
    button_delete=Button(top,text="Delete",bg="Red",fg="white",width=10,command=deletedb )
    button_delete.place(x=250, y=190)
    
    # Disabled Button 
    button_pilihdb.config(state=tk.DISABLED)
    
    # Bind the <Destroy> event to the Toplevel widget
    top.bind("<Destroy>", on_closing) # END -- Top level Database    
    
    
    
def on_database_selection() :
    global mydb,databaselabel
    selected_items =tabel.selection()[0]# mendapatkan item yang dipilih
    values = tabel.item(selected_items)['values'] # mendapatkan nilai dari item yang dipilih
    db=values
    database=db[0]
    mydb= connection_db(database)
    messagebox.showinfo("Information",f"Selected database:{database}")
    databaselabel=Label(app,text="{}".format(database),font="Arial 10",fg="black", bg="white" )
    databaselabel.place(x=30,y=50)
    return
    
    
        
def deletedb():
    # Get the selected database name
    selected_db = tabel.item(tabel.selection())['values'][0]
    
    # Show a confirmation dialog box
    confirm = messagebox.askyesno("Confirm Delete", f"Apakah anda yakin menghapus database '{selected_db}'?")
    
    if confirm:
        # If confirmed, proceed with deleting the database
        mycursor = mydb.cursor()
        db = f"DROP DATABASE {selected_db}"
        mycursor.execute(db)
        pesan = f"Database {selected_db} berhasil dihapus"
        messagebox.showinfo("Info", message=pesan)

    
def on_closing(event):
    global window_closed
    window_closed = True
    button_pilihdb.config(state=tk.NORMAL)

def showCreatedb ():
    # Frame Form Database
    kotak = Frame(top,width=200, height=60, bg='grey')
    kotak.place(x=30, y=70)
    
    # Label Frame Database
    labelNama_db=Label(kotak, text='New Database', fg='white', bg='grey', font="Arial 9 bold")
    labelNama_db.place(x=10, y=5)
    inputNama = Entry(kotak,textvariable=namedb_controller)
    inputNama.place(x=10, y=30)
    
    # Button on Frame form database
    submit=Button(kotak, width=5,text="add", bg="red", fg="white", font="Arial 9 bold",command=createdb)
    submit.place(x=150, y=25)
    
# set data base name 

def createdb() :
    mycursor = mydb.cursor()

    namedb = namedb_controller.get()
    db = ("CREATE DATABASE {}".format(namedb))

    try:
        mycursor.execute(db)
        mycursor.execute("USE {}".format(namedb))
        sql = """CREATE TABLE employeetabel (
            idkry INT AUTO_INCREMENT PRIMARY KEY,
            nama VARCHAR(255) NOT NULL,
            jabatan VARCHAR(255) NOT NULL,
            alamat VARCHAR(255) NOT NULL,
            telepon VARCHAR(255) NOT NULL
        )"""
        mycursor.execute(sql)
        pesan = "Database dan tabel berhasil dibuat"
        messagebox.showinfo("Info", message=pesan)
    except mysql.connector.Error as err:
        pesan = "Sorry..!{}".format(err)
        messagebox.showwarning("WARNING",message=pesan)
        
    
def listdb():
    global mydb, tabel
    mydb=mysql.connector.connect(
        host = "localhost",
        user ="root",
        passwd = "")
    
    tabel.delete(*tabel.get_children())
    mycursor=mydb.cursor()
    mycursor.execute("SHOW DATABASES") # execute the SHOW DATABASES query
    databases= mycursor.fetchall() # get the list of databases 
     
    for db in databases:
        print(db)
        tabel.insert(parent="",index="end", text="",value =(db[0]))
        
# Button on Main Frame
button_pilihdb=Button(app,text="Pilih Database", bg="Blue",fg="white",width=20,command=opendb)
button_pilihdb.place(x=30, y=20)


def showlist_db():
    mycursor =mydb.cursor()
    db =("show databases")
    mycursor.execute(db)
    for (db) in cursor :
        print (db)
# End myFrame 1

app.mainloop()
