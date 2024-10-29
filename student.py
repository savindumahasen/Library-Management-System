from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import pymysql
from tkinter import ttk

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
        
        # Labels
        lbl_index= Label(self.root, text="Index Number",font=("times", 14, "bold"),fg='black',bg="lightblue", bd=0).place(x=10,y=80,width=150)
        lbl_name= Label(self.root, text="Student Name",font=("times", 14, "bold"),fg='black',bg="lightblue", bd=0).place(x=10,y=120,width=150)
        lbl_address= Label(self.root, text="Home Address", font=("times", 14, "bold"),fg='black',bg="lightblue", bd=0).place(x=10,y=160, width=150)
        lbl_contact= Label(self.root, text="Student Telno", font=("times", 14, "bold"),fg='black',bg="lightblue", bd=0).place(x=10,y=200, width=150)
        lbl_email= Label(self.root, text="Student Email", font=("times", 14, "bold"),fg='black',bg="lightblue", bd=0).place(x=10,y=240, width=150)
        lbl_class= Label(self.root, text="Student Class", font=("times", 14, "bold"),fg='black',bg="lightblue", bd=0).place(x=10,y=280, width=150)

        # Variables
        self.var_index = StringVar()
        self.var_name = StringVar()
        self.var_address = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_class = StringVar()

        # Text entries
        Entry(self.root, textvariable=self.var_index, font=("times", 14), fg='black', bg="white", justify=LEFT).place(x=200, y=80, width=250)
        Entry(self.root, textvariable=self.var_name, font=("times", 14), fg='black', bg="white", justify=LEFT).place(x=200, y=120, width=250)
        Entry(self.root, textvariable=self.var_address, font=("times", 14), fg='black', bg="white", justify=LEFT).place(x=200, y=160, width=250)
        Entry(self.root, textvariable=self.var_contact, font=("times", 14), fg='black', bg="white", justify=LEFT).place(x=200, y=200, width=250)
        Entry(self.root, textvariable=self.var_email, font=("times", 14), fg='black', bg="white", justify=LEFT).place(x=200, y=240, width=250)
        Entry(self.root, textvariable=self.var_class, font=("times", 14), fg='black', bg="white", justify=LEFT).place(x=200, y=280, width=250)

        # Button images
        self.btnsave_image = ImageTk.PhotoImage(Image.open("./Images/save.png").resize((110, 55)))
        self.btndelete_image = ImageTk.PhotoImage(Image.open("./Images/delete.png").resize((110, 50)))
        self.btnupdate_image = ImageTk.PhotoImage(Image.open("./Images/update.png").resize((110, 50)))
        self.btnclear_image = ImageTk.PhotoImage(Image.open('./Images/clear.png').resize((110, 50)))

        # Buttons
        Button(self.root, text="Save", command=self.save, cursor='hand1', image=self.btnsave_image, bd=0).place(x=10, y=340, width=100)
        Button(self.root, cursor="hand1", text="Delete",command=self.delete,image=self.btndelete_image, bd=0).place(x=120, y=340, width=100)
        Button(self.root, cursor="hand1", text="Update",command=self.update, image=self.btnupdate_image, bd=0).place(x=230, y=340, width=100)
        Button(self.root, cursor="hand1", text="Clear", image=self.btnclear_image, bd=0).place(x=340, y=340, width=100)

        # Treeview
        Treeview_frame = Frame(self.root, bd=2, relief=RIDGE)
        Treeview_frame.place(x=0, y=400, width=1200, height=150)

        scrolly = Scrollbar(Treeview_frame, orient=VERTICAL)
        scrollx = Scrollbar(Treeview_frame, orient=HORIZONTAL)

        self.treeviewtable = ttk.Treeview(Treeview_frame, columns=("indexno", "name", "address", "contact", "email", "class"),
                                          yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        scrollx.config(command=self.treeviewtable.xview)
        scrolly.config(command=self.treeviewtable.yview)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        self.treeviewtable.heading("indexno", text="IndexNo")
        self.treeviewtable.heading("name", text="Name")
        self.treeviewtable.heading("address", text="Address")
        self.treeviewtable.heading("contact", text="Contact")
        self.treeviewtable.heading("email", text="Email")
        self.treeviewtable.heading("class", text="Class")
        self.treeviewtable["show"] = "headings"

        # Adjust column widths
        self.treeviewtable.column("indexno", width=100)
        self.treeviewtable.column("name", width=150)
        self.treeviewtable.column("address", width=150)
        self.treeviewtable.column("contact", width=100)
        self.treeviewtable.column("email", width=200)
        self.treeviewtable.column("class", width=80)
        self.treeviewtable.pack(fill=BOTH, expand=1)

        # Bind Treeview select
        self.treeviewtable.bind("<ButtonRelease-1>", self.getdata)
        self.displaydata()

    def displaydata(self):
        sqlcon = pymysql.connect(host="localhost", user="root", password="Savindu@123", database="student")
        cur = sqlcon.cursor()
        cur.execute("SELECT indexno, name, address, contact, email, class FROM student")
        result = cur.fetchall()
        self.treeviewtable.delete(*self.treeviewtable.get_children())

        for row in result:
            self.treeviewtable.insert("", END, values=row)
        sqlcon.close()

    def getdata(self, ev):
        # Get the selected item from Treeview
        viewinfo = self.treeviewtable.focus()
        learnerdata = self.treeviewtable.item(viewinfo)
        row = learnerdata['values']
        
        # Ensure row data is present
        if row:
            self.var_index.set(row[0])
            self.var_name.set(row[1])
            self.var_address.set(row[2])
            self.var_contact.set(row[3])
            self.var_email.set(row[4])
            self.var_class.set(row[5])
            

    def save(self):
        sqlcon = pymysql.connect(host="localhost", user="root", password="Savindu@123", database="student")
        cur = sqlcon.cursor()
        try:
            if self.var_index.get() == "":
                messagebox.showerror("Error", "Index Number is Required")
            elif self.var_name.get() == "":
                messagebox.showerror("Error", "Student Name is required")
            elif self.var_address.get() == "":
                messagebox.showerror("Error", "Home Address is required")
            elif self.var_contact.get() == "":
                messagebox.showerror("Error", "Parent Contact is required")
            elif len(self.var_contact.get()) != 10:
                messagebox.showerror("Error", "Contact Number should have 10 numbers")
            elif self.var_email.get() == "":
                messagebox.showerror("Error", "Student Email is required")
            elif self.var_class.get() == "":
                messagebox.showerror("Error", "Student Class is required")
            else:
                cur.execute("INSERT INTO student(indexno, name, address, contact, email, class) VALUES (%s, %s, %s, %s, %s, %s)",
                            (
                                self.var_index.get(),
                                self.var_name.get(),
                                self.var_address.get(),
                                self.var_contact.get(),
                                self.var_email.get(),
                                self.var_class.get(),
                            ))
                sqlcon.commit()
                messagebox.showinfo("Success", "Data is inserted successfully!")
                self.displaydata()
                sqlcon.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")

    ## Update the record sucessfully
    def update(self):
        sqlcon = pymysql.connect(host="localhost", user="root", password="Savindu@123", database="student")
        cur = sqlcon.cursor()
        cur.execute("UPDATE student SET name=%s,address=%s,contact=%s,email=%s,class=%s WHERE indexno=%s",
                    ( 
                           self.var_name.get(), 
                           self.var_address.get(),
                           self.var_contact.get(),
                           self.var_email.get(),
                           self.var_class.get(),
                           self.var_index.get()

                    ))
        sqlcon.commit()
        messagebox.showinfo("Success", "Record is updated successfully!")
        self.displaydata()
        sqlcon.close()

    def delete(self):
        sqlconn =pymysql.connect(host="localhost", user="root", password="Savindu@123", database="student")
        cur=sqlconn.cursor()
        cur.execute("DELETE FROM student WHERE indexno=%s",
                        (
                            self.var_index.get()
                        ))
        sqlconn.commit()
        messagebox.showinfo("Success", "Record is deleteed successfully!")
        self.displaydata()
        sqlconn.close()
        
        
             


# Running the app
root = Tk()
obj = Student(root)
root.mainloop()
