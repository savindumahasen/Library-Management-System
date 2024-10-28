from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import pymysql
from tkinter import ttk,messagebox
class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x600+200+150")
        self.root.title("Student Management System")
        self.root.resizable(False, False)

        # Load and display the image
        self.photo_image = ImageTk.PhotoImage(Image.open("./Images/student.jpeg").resize((600, 500)))
        self.lbl_photo_image = Label(self.root, image=self.photo_image, bd=0)
        self.lbl_photo_image.place(x=500, y=0)

        # Title at the top
        title = Label(self.root, text="Student Management System", font=("times", 30, "bold"), bg="lightblue", fg="black")
        title.pack(side=TOP, fill=X)
        
        # Add the labels
        lbl_index= Label(self.root, text="Index Number",font=("times", 14, "bold"),fg='black',bg="lightblue", bd=0).place(x=10,y=80,width=150)
        lbl_name= Label(self.root, text="Student Name",font=("times", 14, "bold"),fg='black',bg="lightblue", bd=0).place(x=10,y=120,width=150)
        lbl_address= Label(self.root, text="Home Address", font=("times", 14, "bold"),fg='black',bg="lightblue", bd=0).place(x=10,y=160, width=150)
        lbl_contact= Label(self.root, text="Student Telno", font=("times", 14, "bold"),fg='black',bg="lightblue", bd=0).place(x=10,y=200, width=150)
        lbl_email= Label(self.root, text="Student Email", font=("times", 14, "bold"),fg='black',bg="lightblue", bd=0).place(x=10,y=240, width=150)
        lbl_class= Label(self.root, text="Student Class", font=("times", 14, "bold"),fg='black',bg="lightblue", bd=0).place(x=10,y=280, width=150)


        ## Variables
        self.var_index=StringVar()
        self.var_name=StringVar()
        self.var_address=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_class=StringVar()

        ## text entries

        entry_index = Entry(self.root,textvariable=self.var_index,font=("times", 14),fg='black',bg="white", justify=LEFT)
        entry_index.place(x=200,y=80, width=250)
        entry_index.focus()

        
        entry_name = Entry(self.root,textvariable=self.var_name,font=("times", 14),fg='black',bg="white", justify=LEFT)
        entry_name.place(x=200,y=120, width=250)
        

         
        entry_address = Entry(self.root,textvariable=self.var_address,font=("times", 14),fg='black',bg="white", justify=LEFT)
        entry_address.place(x=200,y=160, width=250)
     
         
        entry_contact = Entry(self.root,textvariable=self.var_contact,font=("times", 14),fg='black',bg="white", justify=LEFT)
        entry_contact.place(x=200,y=200, width=250)
     
         
        entry_email = Entry(self.root,textvariable=self.var_email,font=("times", 14),fg='black',bg="white", justify=LEFT)
        entry_email.place(x=200,y=240, width=250)
        
         
        entry_class = Entry(self.root,textvariable=self.var_class,font=("times", 14),fg='black',bg="white", justify=LEFT)
        entry_class.place(x=200,y=280, width=250)


        self.btnsave_image = ImageTk.PhotoImage(Image.open("./Images/save.png").resize((110,55)))
        self.btndelete_image = ImageTk.PhotoImage(Image.open("./Images/delete.png").resize((110,50)))
        self.btnupdate_image =ImageTk.PhotoImage(Image.open("./Images/update.png").resize((110,50)))
        self.btnclear_image =ImageTk.PhotoImage(Image.open('./Images/clear.png').resize((110,50)))

        ## Buttons
        btn_save =Button(self.root,text="Save", command=self.save,cursor='hand1', image=self.btnsave_image, bd=0)
        btn_save.place(x=10, y=340, width=100)

        btn_delete = Button( self.root, cursor="hand1",text="Delete", image=self.btndelete_image, bd=0)
        btn_delete.place(x=120, y=340, width=100)

        btn_update = Button(self.root,cursor="hand1", text="Update", image=self.btnupdate_image, bd=0)
        btn_update.place(x=230, y=340, width=100)

        
        btn_clear = Button(self.root,cursor="hand1", text="Clear", image=self.btnclear_image, bd=0)
        btn_clear.place(x=340, y=340, width=100)

           ## Variables
        self.var_index=StringVar()
        self.var_name=StringVar()
        self.var_address=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_class=StringVar()
        ## Treeview  ##

        Treeview_frame = Frame(self.root, bd=2, relief=RIDGE)
        Treeview_frame.place(x=0, y=400, width=1200, height=150)

        scrolly=Scrollbar(Treeview_frame, orient=VERTICAL)
        scrollx =Scrollbar(Treeview_frame,orient=HORIZONTAL)

        self.treeviewtable=ttk.Treeview(Treeview_frame, columns=("indexno","name","address","contact","email","class"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)

        scrollx.config(command=self.treeviewtable.xview)
        
        scrolly.config(command=self.treeviewtable.yview)


        self.treeviewtable.heading("indexno",text="IndexNo")
        self.treeviewtable.heading("name",text="Name")
        self.treeviewtable.heading("address",text="Address")
        self.treeviewtable.heading("contact",text="Contact")
        self.treeviewtable.heading("email",text="Email")
        self.treeviewtable.heading("class",text="Class")


        self.treeviewtable["show"]="headings"
        self.treeviewtable.column("indexno",width=-10)
        self.treeviewtable.column("name",width=-10)
        self.treeviewtable.column("address", width=-10)
        self.treeviewtable.column("contact", width=-10)
        self.treeviewtable.column("email",width=-10)
        self.treeviewtable.column("class",width=-10)


        self.treeviewtable.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.treeviewtable.yview)
        #self.treeviewtable.bind("<ButtonRelease-1>",self.getdata)
        self.displaydata()

    def displaydata(self):
         
        sqlcon =pymysql.connect(host="localhost", user="root",password="Savindu@123", database="student")
        cur=sqlcon.cursor()
        cur.execute("SELECT indexno,name,address,contact,email,class FROM student")
        result=cur.fetchall()


        self.treeviewtable.delete(*self.treeviewtable.get_children())

        for row in result:
             self.treeviewtable.insert("",END,values=row)

         
         

    def save(self):

        sqlcon =pymysql.connect(host="localhost", user="root",password="Savindu@123", database="student")
        cur=sqlcon.cursor()
        try:
            if self.var_index.get()=="":
                messagebox.showerror("Error","Index Number is Required")
            elif self.var_name.get()=="":
                 messagebox.showerror("Error","Student Name is required")
            elif self.var_address.get()=="":
                 messagebox.showerror("Error","Home Address is required")
            elif self.var_contact.get()=="":
                 messagebox.showerror("Error","Parent Contact is required")
            elif len(self.var_contact.get())!=10:
                 messagebox.showerror("Error","Contact Number should have 10 numers")
            elif self.var_email.get()=="":
                 messagebox.showerror("Error","Student Email is required")
            elif self.var_class.get()=="":
                 messagebox.showerror("Error","Student Class is required")
            else:
                cur.execute("INSERT INTO student(indexno,name,address,contact,email,class) VALUES (%s,%s,%s,%s,%s,%s)",
                (
                  self.var_index.get(),
                  self.var_name.get(),
                  self.var_address.get(),
                  self.var_contact.get(),
                  self.var_email.get(),
                  self.var_class.get(),

                ))
                sqlcon.commit()
                messagebox.showinfo("Sucess","Data is inserted sucessfully........!")
                sqlcon.close()
                print("Close the database connection sucessfully")
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}")

         
     


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
