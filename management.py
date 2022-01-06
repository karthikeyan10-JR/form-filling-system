from tkinter import *
from tkinter import ttk
import mysql.connector
import sys
import messagebox

class student():
    def __init__(self,root):
        self.root = root
        self.root.title("form registration")
        self.root.geometry("1350x700+0+0")
        title = Label(self.root, text="registration form",bd=9,relief=GROOVE, font=("times new roman",50,"bold"), bg="blue",fg="white")
        title.pack(side=TOP,fill=X)
#=================================================== variable================================================
        self.roll_no_var = StringVar()
        self.name_var = StringVar()
        self.branch_var = StringVar()
        self.section_var = StringVar()
        self.age_var = StringVar()
        self.number_var = StringVar()
        self.address_var = StringVar()
        self.search_by = StringVar()
        self.search_var = StringVar()
        
#===========================================side frame==========================================================
        
        manage_frame = Frame(self.root,bd=4,relief=RIDGE,bg="gray")
        manage_frame.place(x=20,y=100,width=450,height=620)
        m_title = Label(manage_frame,text="manage student",bg="blue",fg="gray", font=("times new roman",40,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)


        
        lbl_roll_no = Label(manage_frame,text="roll_no",bg="gray",fg="black", font=("times new roman",20,"bold"))
        lbl_roll_no.grid(row=1,column=0,pady=10,padx=20,sticky="w")
        txt_roll_no = Entry(manage_frame,textvariable=self.roll_no_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll_no.grid(row=1,column=1,pady=10,padx=20,sticky="w")


        lbl_name = Label(manage_frame,text="name",bg="gray",fg="black", font=("times new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")
        txt_name = Entry(manage_frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_branch = Label(manage_frame,text="branch",bg="gray",fg="black", font=("times new roman",20,"bold"))
        lbl_branch.grid(row=3,column=0,pady=10,padx=20,sticky="w")
        combo_branch = ttk.Combobox(manage_frame,textvariable=self.branch_var,font=("times new roman",13,"bold") ,state='readonly')
        combo_branch['values']=("ECE","CSE","IT","EEE","AIDS","CSBS","MECH")
        combo_branch.grid(row=3,column=1,pady=20,padx=10)


        lbl_section = Label(manage_frame,text="section",bg="gray",fg="black", font=("times new roman",20,"bold"))
        lbl_section.grid(row=4,column=0,pady=10,padx=20,sticky="w")
        txt_section = Entry(manage_frame,textvariable=self.section_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_section.grid(row=4,column=1,pady=10,padx=20,sticky="w")

        
        lbl_age = Label(manage_frame,text="age",bg="gray",fg="black", font=("times new roman",20,"bold"))
        lbl_age.grid(row=5,column=0,pady=10,padx=20,sticky="w")
        txt_age = Entry(manage_frame,textvariable=self.age_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_age.grid(row=5,column=1,pady=10,padx=20,sticky="w")


        lbl_number = Label(manage_frame,text="number",bg="gray",fg="black", font=("times new roman",20,"bold"))
        lbl_number.grid(row=6,column=0,pady=10,padx=20,sticky="w")
        txt_number = Entry(manage_frame,textvariable=self.number_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_number.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        lbl_address = Label(manage_frame,text="address",bg="gray",fg="black", font=("times new roman",20,"bold"))
        lbl_address.grid(row=7,column=0,pady=10,padx=20,sticky="w")
        self.txt_address = Text(manage_frame,width = 25,height = 3,font=("times new roman",10,"bold"))
        self.txt_address.grid(row=7,column=1,pady=10,padx=20,sticky="w")


        
#===============================================button============================================================


        btn_frame=Frame(manage_frame,bd=3,relief=RIDGE,bg="black")
        btn_frame.place(x=15,y=550,width=526)

        addbtn = Button(btn_frame,text="add",width=10,command=self.add_student).grid(row=0,column=0,padx=10,pady=10)
        dbtn = Button(btn_frame,text="delete",width=10,command=self.delete).grid(row=0,column=1,padx=10,pady=10)
        updbtn = Button(btn_frame,text="update",width=10,command=self.update).grid(row=0,column=2,padx=10,pady=10)
        clearbtn = Button(btn_frame,text="clear",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)


#=============================================detail_frame========================================================

        
        detail_frame = Frame(self.root,bd=4,relief=RIDGE,bg="gray")
        detail_frame.place(x=500,y=100,width=850,height=620)
        table_frame = Frame(detail_frame,bd=4,relief=RIDGE,bg="white")
        table_frame.place(x=10,y=20,width=820,height=550)

        
#============================================scroll_bar==========================================================


        
        scroll_x = Scrollbar(table_frame,orient = HORIZONTAL)
        scroll_y = Scrollbar(table_frame,orient = VERTICAL)

        self.student_table= ttk.Treeview(table_frame,column =("roll_no","name","branch","section","age","number","address"),xscrollcommand=scroll_x,yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("roll_no" , text = "roll_no")
        self.student_table.heading("name" , text = "name")
        self.student_table.heading("branch" , text = "branch")
        self.student_table.heading("section" , text = "section")
        self.student_table.heading("age" , text = "age")
        self.student_table.heading("number" , text = "number")
        self.student_table.heading("address" , text = "address")        

        self.student_table['show']='headings'
        self.student_table.column("roll_no" , width=100)
        self.student_table.column("name" , width=100)
        self.student_table.column("branch" , width=100)
        self.student_table.column("section" , width=100)
        self.student_table.column("age" , width=100)
        self.student_table.column("number" , width=100)
        self.student_table.column("address" , width=150)
        

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.getcursor)
        self.fetch_data()
        

    def add_student(self):
        roll_no=self.roll_no_var.get()
        name=self.name_var.get()
        bran=self.branch_var.get()
        section=self.section_var.get()
        age=self.age_var.get()
        num=self.number_var.get()
        adde=self.txt_address.get('1.0',END)

        if (roll_no == "" or name == ""):
            messagebox.showerror("error","all field are required to fill")
        else:
          mydb = mysql.connector.connect(host="localhost",user="root",password="123456789",database="student_details")
          obj=mydb.cursor()
          insert = "insert into goform(roll_no,name,branch,section,age,number,address)\
          values (%s,%s,%s,%s,%s,%s,%s)"
          val = (roll_no, name, bran, section, age, num, adde)
          obj.execute(insert, val)
          mydb.commit()
          self.fetch_data()
          self.clear()
          mydb.close()
          messagebox.showinfo("added","data added successfully")
        
    def fetch_data(self):
        
        mydb = mysql.connector.connect(host="localhost",user="root",password="123456789",database="student_details")
        obj=mydb.cursor()
        obj.execute("select * from goform")
        rows=obj.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            mydb.commit
        mydb.close()


    def clear(self):
        self.roll_no_var.set("")
        self.name_var.set("")
        self.branch_var.set("")
        self.section_var.set("")
        self.age_var.set("")
        self.number_var.set("")
        self.txt_address.delete("1.0",END)

    def getcursor(self,ev):
        curosor_row = self.student_table.focus()
        contents = self.student_table.item(curosor_row)
        row=contents['values']
        self.roll_no_var.set(row[0])
        self.name_var.set(row[1])
        self.branch_var.set(row[2])
        self.section_var.set(row[3])
        self.age_var.set(row[4])
        self.number_var.set(row[5])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[6])


    def update(self):
        roll_no=self.roll_no_var.get()
        name=self.name_var.get()
        bran=self.branch_var.get()
        section=self.section_var.get()
        age=self.age_var.get()
        num=self.number_var.get()
        adde=self.txt_address.get('1.0',END)
        mydb = mysql.connector.connect(host="localhost",user="root",password="123456789",database="student_details")
        obj=mydb.cursor()
        obj.execute("update goform SET name=%s,branch=%s,section=%s,age=%s,number=%s,address=%s WHERE roll_no=%s",(name,
                                                                                                        bran,
                                                                                                        section,
                                                                                                        age,
                                                                                                        num,
                                                                                                        adde,
                                                                                                        roll_no))
        mydb.commit()
        self.fetch_data()
        self.clear()
        mydb.close()
        messagebox.showinfo("updated","data updated successfully")

        
    def delete(self):
        mydb = mysql.connector.connect(host="localhost",user="root",password="123456789",database="student_details")
        obj=mydb.cursor()
        bid = self.roll_no_var.get()
        deleteSql = "delete from goform where roll_no = '"+bid+"'"
        obj.execute(deleteSql)
        mydb.commit()
        self.clear()
        self.fetch_data()
        mydb.close()
        messagebox.showinfo("updated","data updated successfully")
        
        
    def search_data(self):
        mydb = mysql.connector.connect(host="localhost",user="root",password="123456789",database="student_details")
        obj=mydb.cursor()
        bid = self.search_var.get()
        search = "select * from goform where roll_no = '"+bid+"'"
        obj.execute(search)
        mydb.commit
        mydb.close()

        
       
        

root=Tk()
obj = student(root)
root.mainloop()
