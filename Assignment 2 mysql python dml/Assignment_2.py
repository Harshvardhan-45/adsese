import tkinter as tk
import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="Hp452002@",port="3306", database="2020BTECS00050")
print("successful")
cursor = conn.cursor();


master = tk.Tk()
tk.Label(master,text="First Name").grid(row=0) 
         
tk.Label(master,text="Last Name").grid(row=1)
         

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

def Create():
    query = """
        CREATE TABLE USER(
            firstname VARCHAR(40) NOT NULL,
            lastname VARCHAR(40) NOT NULL
        )
    """
    
    cursor.execute(query)
    print("Table created successfully")

    
        

def Insert():
    first_name= e1.get()
    last_name=e2.get()
    query = """INSERT INTO USER VALUES( %s, %s)"""
    
    cursor.execute(query,(first_name,last_name))
    print("Inserted successfully")
    
    
def Show():
    
    
    cursor.execute("SELECT * FROM USER")
    for row in cursor:
        print(row)
    
def Update():
    first_name=e1.get()
    last_name=e2.get()
   
    query="""UPDATE USER
             SET lastname = %s
             WHERE firstname = %s"""
    
    cursor.execute(query,(last_name,first_name))
    
def Delete():
    query = """
        DROP TABLE USER 
    """
    
    cursor.execute(query)
    print("Table deleted successfully")

    


tk.Button(master,text='Create',command=Create).grid(row=3, column=0,sticky=tk.W,pady=4)  
tk.Button(master,text='Insert', command=Insert).grid(row=3,column=1, sticky=tk.W,pady=4)
tk.Button(master,text='Show', command=Show).grid(row=3,column=2, sticky=tk.W,pady=4)
tk.Button(master,text='Update', command=Update).grid(row=3,column=3, sticky=tk.W,pady=4)
tk.Button(master,text='Delete', command=Delete).grid(row=3,column=4, sticky=tk.W,pady=4)           
          
                                     
                                    
   

                                                        
                                                      
                                                       

tk.mainloop()