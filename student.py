from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x500+200+100")
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

        entry_index = Entry(self.root,font=("times", 14),fg='black',bg="white", justify=LEFT)
        entry_index.place(x=200,y=80, width=250)
        entry_index.focus()

        
        entry_name = Entry(self.root,font=("times", 14),fg='black',bg="white", justify=LEFT)
        entry_name.place(x=200,y=120, width=250)
        

         
        entry_address = Entry(self.root,font=("times", 14),fg='black',bg="white", justify=LEFT)
        entry_address.place(x=200,y=160, width=250)
     
         
        entry_contact = Entry(self.root,font=("times", 14),fg='black',bg="white", justify=LEFT)
        entry_contact.place(x=200,y=200, width=250)
     
         
        entry_email = Entry(self.root,font=("times", 14),fg='black',bg="white", justify=LEFT)
        entry_email.place(x=200,y=240, width=250)
        
         
        entry_class = Entry(self.root,font=("times", 14),fg='black',bg="white", justify=LEFT)
        entry_class.place(x=200,y=280, width=250)


        self.btnsave_image = ImageTk.PhotoImage(Image.open("./Images/save.png").resize((110,55)))
        self.btndelete_image = ImageTk.PhotoImage(Image.open("./Images/delete.png").resize((110,50)))
        self.btnupdate_image =ImageTk.PhotoImage(Image.open("./Images/update.png").resize((110,50)))
        self.btnclear_image =ImageTk.PhotoImage(Image.open('./Images/clear.png').resize((110,50)))

        ## Buttons
        btn_save =Button(self.root,text="Save",cursor='hand1', image=self.btnsave_image, bd=0)
        btn_save.place(x=10, y=340, width=100)

        btn_delete = Button( self.root, cursor="hand1",text="Delete", image=self.btndelete_image, bd=0)
        btn_delete.place(x=120, y=340, width=100)

        btn_update = Button(self.root,cursor="hand1", text="Update", image=self.btnupdate_image, bd=0)
        btn_update.place(x=230, y=340, width=100)

        
        btn_clear = Button(self.root,cursor="hand1", text="Clear", image=self.btnclear_image, bd=0)
        btn_clear.place(x=340, y=340, width=100)

         
     


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
