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
        self.photo_image = ImageTk.PhotoImage(Image.open("schooling.jpg").resize((550, 500)))
        self.lbl_photo_image = Label(self.root, image=self.photo_image, bd=0)
        self.lbl_photo_image.place(x=600, y=0)

        # Title at the top
        title = Label(self.root, text="Student Management System", font=("times", 30, "bold"), bg="lightblue", fg="black")
        title.pack(side=TOP, fill=X)
        
        # Add the labels
        lbl_index= Label(self.root, text="Index Number",font=("times", 14, "bold"),fg='black',bg="lightblue").place(x=10,y=80,width=150)
        lbl_name= Label(self.root, text="Student Name",font=("times", 14, "bold"),fg='black',bg="lightblue").place(x=10,y=120,width=150)
        lbl_address= Label(self.root, text="Home Address", font=("times", 14, "bold"),fg='black',bg="lightblue").place(x=10,y=160, width=150)
        lbl_contact= Label(self.root, text="Student Telno", font=("times", 14, "bold"),fg='black',bg="lightblue").place(x=10,y=200, width=150)
        lbl_email= Label(self.root, text="Student Email", font=("times", 14, "bold"),fg='black',bg="lightblue").place(x=10,y=240, width=150)
        lbl_class= Label(self.root, text="Student Class", font=("times", 14, "bold"),fg='black',bg="lightblue").place(x=10,y=280, width=150)


        ## Variables
        self.var_index=StringVar()
        self.var_name=StringVar()
        self.var_address=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_class=StringVar()

        ## text entries

        entry_index = Entry(self.root,font=("times", 14),fg='black',bg="white", justify=LEFT)
        entry_index.place(x=200,y=80, width=150)
        entry_index.focus()

        
        entry_name = Entry(self.root,font=("times", 14),fg='black',bg="white", justify=LEFT)
        entry_name.place(x=200,y=120, width=150)
        

         
        entry_address = Entry(self.root,font=("times", 14),fg='black',bg="white", justify=LEFT)
        entry_address.place(x=200,y=160, width=150)
     
         
        entry_contact = Entry(self.root,font=("times", 14),fg='black',bg="white", justify=LEFT)
        entry_contact.place(x=200,y=200, width=150)
     
         
        entry_email = Entry(self.root,font=("times", 14),fg='black',bg="white", justify=LEFT)
        entry_email.place(x=200,y=240, width=150)
        
         
        entry_class = Entry(self.root,font=("times", 14),fg='black',bg="white", justify=LEFT)
        entry_class.place(x=200,y=280, width=150)
     


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
