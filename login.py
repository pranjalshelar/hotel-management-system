from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import psycopg2
from tkinter import messagebox
from register import Register
from HMS import HotelManagementSystem
import os

DB_CONFIG = {
    'host': 'localhost',
    'database': 'postgres',
    'user': 'postgres',
    'password': 'psql', #psql
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
        self.txtpass = ttk.Entry(frame, font=('times new roman',15,'bold'))
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

        forgetpass = Button(frame, text='Forget Password', command=self.forgot_password_window,
                          font=('times new roman',10,'bold'), cursor='hand2', bg='black',
                          fg='white', borderwidth=0, activeforeground='white',
                          activebackground='black')
        forgetpass.place(x=11, y=370, width=160)

        test_db_btn = Button(self.root, text="Test DB Connection", 
                           command=self.test_db_connection,
                           font=('times new roman',10,'bold'),
                           bg='black', fg='white')
        test_db_btn.place(x=10, y=10)

    def get_db_connection(self):
        try:
            conn = psycopg2.connect(**DB_CONFIG)
            return conn
        except psycopg2.Error as err:
            messagebox.showerror("Database Error", f"Failed to connect to database: {err}")
            return None

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.txtuser.get()=="kapu" and self.txtpass.get()=="ashu":
            messagebox.showinfo("Success","Welcome to Hotel Management System")
            self.new_window=Toplevel(self.root)
            self.app=HotelManagementSystem(self.new_window)
        else:
            conn = self.get_db_connection()
            if conn:
                try:
                    with conn.cursor() as my_cursor:
                        my_cursor.execute("SELECT * FROM register WHERE email=%s AND password=%s",(
                                            self.txtuser.get(),
                                            self.txtpass.get()
                        ))
                        row = my_cursor.fetchone()
                        if row==None:
                            messagebox.showerror("Error","Invalid Username & Password")
                        else:
                            open_main=messagebox.askyesno("YesNo","Access only admin")
                            if open_main>0:
                                self.new_window=Toplevel(self.root)
                                self.app=HotelManagementSystem(self.new_window)
                            else:
                                if not open_main:
                                    return
                except psycopg2.Error as err:
                    messagebox.showerror("Database Error", f"Error: {err}")
                finally:
                    conn.close()

    def test_db_connection(self):
        try:
            conn = psycopg2.connect(**DB_CONFIG)
            messagebox.showinfo("Success", "Database connection successful!")
            conn.close()
        except psycopg2.Error as err:
            messagebox.showerror("Database Error", 
                               f"Failed to connect to database: {err}\n\n"
                               "Please make sure:\n"
                               "1. PostgreSQL server is running\n"
                               "2. Database 'hotel_management' exists\n"
                               "3. Username and password are correct")

    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn = self.get_db_connection()
            if conn:
                try:
                    with conn.cursor() as my_cursor:
                        query = "SELECT * FROM register WHERE email=%s AND security_q=%s AND security_a=%s"
                        value = (self.txtuser.get(), self.combo_security_Q.get(), self.txt_security.get())
                        my_cursor.execute(query, value)
                        row = my_cursor.fetchone()
                        if row==None:
                            messagebox.showerror("Error","Please enter correct Answer",parent=self.root2)
                        else:
                            query = "UPDATE register SET password=%s WHERE email=%s"
                            value = (self.txt_newpass.get(), self.txtuser.get())
                            my_cursor.execute(query, value)
                            conn.commit()
                            messagebox.showinfo("Info","Your password has been reset, please login with new password",parent=self.root2)
                            self.root2.destroy()
                except psycopg2.Error as err:
                    messagebox.showerror("Database Error", f"Error: {err}")
                finally:
                    conn.close()

    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Write the Email address to reset password")
        else:
            conn = self.get_db_connection()
            if conn:
                try:
                    with conn.cursor() as my_cursor:
                        query = "SELECT * FROM register WHERE email=%s"
                        value = (self.txtuser.get(),)
                        my_cursor.execute(query, value)
                        row = my_cursor.fetchone()
                        if row==None:
                            messagebox.showerror("Error","Please enter the valid username")
                        else:
                            conn.close()
                            self.root2=Toplevel()
                            self.root2.title("Forgot Password")
                            self.root2.geometry("340x450+610+170")

                            l=Label(self.root2,text="Forgot Password",font=('times new roman',15,'bold'),fg='white',bg='black')
                            l.place(x=0,y=10,relwidth=1)

                            security_Q=Label(self.root2,text="Select Security Question",font=('times new roman',15,'bold'),fg='black',bg='white')
                            security_Q.place(x=50,y=80)

                            self.combo_security_Q=ttk.Combobox(self.root2,font=('times new roman',15),state='readonly')
                            self.combo_security_Q["values"]=("Select","Your Birth Place","Your Pet Name","Your Favourit Place","Your Dearest Person","Your Favourite Flowers","Your Favourite Book")
                            self.combo_security_Q.place(x=50,y=110,width=250)
                            self.combo_security_Q.current(0)

                            security_A=Label(self.root2,text="Security Answer",font=('times new roman',15,'bold'),fg='black',bg='white')
                            security_A.place(x=50,y=150)

                            self.txt_security=ttk.Entry(self.root2,font=('times new roman',15))
                            self.txt_security.place(x=50,y=180,width=250)

                            new_password=Label(self.root2,text="New Password",font=('times new roman',15,'bold'),fg='black',bg='white')
                            new_password.place(x=50,y=220)

                            self.txt_newpass=ttk.Entry(self.root2,font=('times new roman',15))
                            self.txt_newpass.place(x=50,y=250,width=250)

                            btn=Button(self.root2,text="Reset",command=self.reset_pass,font=('times new roman',15),fg='white',bg='green')
                            btn.place(x=100,y=290)

                            backbtn=Button(self.root2,command=self.back,text='Back',font=('times new roman',15,'bold'),bd=3,cursor='hand2',bg='dark red',fg='white',activeforeground='white',activebackground='dark red')
                            backbtn.place(x=110,y=340,width=120,height=35)
                except psycopg2.Error as err:
                    messagebox.showerror("Database Error", f"Error: {err}")
                finally:
                    conn.close()

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def back(self):
        self.root2.destroy()

if __name__ =="__main__":
    root=Tk()
    obj=Login_Window(root)
    root.mainloop()    