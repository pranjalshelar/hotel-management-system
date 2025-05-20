from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import psycopg2
from tkinter import messagebox
from register import Register
from HMS import HotelManagementSystem
import os
from db_config import get_db_connection

DB_CONFIG = {
    'host': 'localhost',
    'database': 'postgres',
    'user': 'postgres',
    'password': 'psql',
    'port': '5432'
}

def update_db_config(new_password):
    global DB_CONFIG
    DB_CONFIG['password'] = new_password

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        self.root.attributes('-fullscreen',True)

        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.images_dir = os.path.join(self.current_dir, 'images')

        try:
            img_path = os.path.join(self.images_dir, "im2.jpg")
            img = Image.open(img_path)
            img = img.resize((1550,900), Image.Resampling.LANCZOS)
            self.photoimg = ImageTk.PhotoImage(img)

            labling = Label(self.root, image=self.photoimg)
            labling.place(x=0, y=0, width=1550, height=900)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load background image: {str(e)}")

        frame = Frame(self.root, bg='black')
        frame.place(x=610, y=170, width=340, height=450)

        try:
            img1_path = os.path.join(self.images_dir, "user.png")
            img1 = Image.open(img1_path)
            img1 = img1.resize((100,100), Image.Resampling.LANCZOS)
            self.photoimg1 = ImageTk.PhotoImage(img1)

            labling1 = Label(self.root, image=self.photoimg1, bg="black", borderwidth=0)
            labling1.place(x=730, y=175, width=100, height=100)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load user icon: {str(e)}")

        get_str = Label(frame, text='Get Started', font=('times new roman',20,'bold'), fg='white', bg='black')
        get_str.place(x=95, y=100)

        username = Label(frame, text="Username:", font=('times new roman',15,'bold'), fg='white', bg='black')
        username.place(x=70, y=155)
        self.txtuser = ttk.Entry(frame, font=('times new roman',15,'bold'))
        self.txtuser.place(x=40, y=180, width=270)

        password = Label(frame, text="Password:", font=('times new roman',15,'bold'), fg='white', bg='black')
        password.place(x=70, y=225)
        self.txtpass = ttk.Entry(frame, font=('times new roman',15,'bold'), show="*")
        self.txtpass.place(x=40, y=250, width=270)

        try:
            img2_path = os.path.join(self.images_dir, "login.png")
            img2 = Image.open(img2_path)
            img2 = img2.resize((25,25), Image.Resampling.LANCZOS)
            self.photoimg2 = ImageTk.PhotoImage(img2)

            labling2 = Label(self.root, image=self.photoimg2, bg="black", borderwidth=0)
            labling2.place(x=650, y=323, width=25, height=25)

            img3_path = os.path.join(self.images_dir, "pass.png")
            img3 = Image.open(img3_path)
            img3 = img3.resize((25,25), Image.Resampling.LANCZOS)
            self.photoimg3 = ImageTk.PhotoImage(img3)

            labling3 = Label(self.root, image=self.photoimg3, bg="black", borderwidth=0)
            labling3.place(x=650, y=394, width=25, height=25)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load icons: {str(e)}")

        loginbtn = Button(frame, command=self.login, text='Login', font=('times new roman',15,'bold'),
                         bd=3, cursor='hand2', bg='dark red', fg='white',
                         activeforeground='white', activebackground='dark red')
        loginbtn.place(x=110, y=300, width=120, height=35)

        registerbtn = Button(frame, text='New User Register', command=self.register_window,
                           font=('times new roman',10,'bold'), cursor='hand2', bg='black',
                           fg='white', borderwidth=0, activeforeground='white',
                           activebackground='black')
        registerbtn.place(x=18, y=350, width=160)

        exitbtn = Button(frame, text='Exit', command=self.exit_application,
                        font=('times new roman',10,'bold'), cursor='hand2', bg='black',
                        fg='white', borderwidth=0, activeforeground='white',
                        activebackground='black')
        exitbtn.place(x=18, y=380, width=160)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return

        try:
            conn = get_db_connection()
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s",
                             (self.txtuser.get(), self.txtpass.get()))
                user = cursor.fetchone()
                
                if user:
                    messagebox.showinfo("Success", "Welcome to Hotel Management System")
                    self.root.withdraw()
                    self.new_window = Toplevel(self.root)
                    self.app = HotelManagementSystem(self.new_window)
                else:
                    messagebox.showerror("Error", "Invalid Username & Password")
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Login failed: {str(e)}")

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def exit_application(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.root.destroy()

if __name__ =="__main__":
    root=Tk()
    obj=Login_Window(root)
    root.mainloop()    