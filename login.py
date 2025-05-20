from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from tkinter import messagebox
from register import Register
from HMS import HotelManagementSystem
import os
from db_config import execute_query
from db_config import get_db_connection

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

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.txtuser.get()=="kapu" and self.txtpass.get()=="ashu":
            messagebox.showinfo("Success","Welcome to Hotel Management System")
            self.new_window=Toplevel(self.root)
            self.app=HotelManagementSystem(self.new_window)
        else:
            query = "SELECT * FROM register WHERE email=%s AND password=%s"
            params = (self.txtuser.get(), self.txtpass.get())
            row = execute_query(query, params, fetch=True)
            
            if not row:
                messagebox.showerror("Error","Invalid Username & Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return

    def test_db_connection(self):
        conn = get_db_connection()
        if conn:
            messagebox.showinfo("Success", "Database connection successful!")
            conn.close()
        else:
            messagebox.showerror("Database Error", 
                               "Failed to connect to database.\n\n"
                               "Please make sure:\n"
                               "1. PostgreSQL server is running\n"
                               "2. Database 'hotel_management' exists\n"
                               "3. Username and password are correct")

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error", "Please enter the Email Address to reset password!")
        else:
            query = "SELECT * FROM register WHERE email=%s"
            row = execute_query(query, (self.txtuser.get(),), fetch=True)
            
            if not row:
                messagebox.showerror("Error", "Please enter the valid Email Address!")
            else:
                conn = get_db_connection()
                if conn:
                    cursor = conn.cursor()
                    cursor.execute("SELECT * FROM register WHERE email=%s", (self.txtuser.get(),))
                    row = cursor.fetchone()
                    
                    if row:
                        security_question = row[4]  # Assuming security question is at index 4
                        messagebox.showinfo("Security Question", f"Your security question is: {security_question}")
                        
                        # Create a new window for security answer
                        self.new_window = Toplevel(self.root)
                        self.new_window.title("Reset Password")
                        self.new_window.geometry("400x300+500+200")
                        self.new_window.focus_force()
                        self.new_window.grab_set()
                        
                        # Security answer entry
                        Label(self.new_window, text="Security Answer:", font=("times new roman", 15, "bold")).place(x=50, y=50)
                        self.txt_security_answer = ttk.Entry(self.new_window, font=("times new roman", 15))
                        self.txt_security_answer.place(x=50, y=80, width=250)
                        
                        # New password entry
                        Label(self.new_window, text="New Password:", font=("times new roman", 15, "bold")).place(x=50, y=120)
                        self.txt_new_password = ttk.Entry(self.new_window, font=("times new roman", 15))
                        self.txt_new_password.place(x=50, y=150, width=250)
                        
                        # Reset button
                        Button(self.new_window, text="Reset Password", command=lambda: self.reset_password(row[4], self.txt_security_answer.get(), self.txt_new_password.get()), 
                               font=("times new roman", 15, "bold"), bg="green", fg="white").place(x=50, y=200)
                        
                    cursor.close()
                    conn.close()

    def reset_password(self, security_question, security_answer, new_password):
        if security_answer == "" or new_password == "":
            messagebox.showerror("Error", "All fields are required!", parent=self.new_window)
        else:
            query = "SELECT * FROM register WHERE email=%s AND securityQ=%s AND securityA=%s"
            row = execute_query(query, (self.txtuser.get(), security_question, security_answer), fetch=True)
            
            if not row:
                messagebox.showerror("Error", "Please enter the correct Answer!", parent=self.new_window)
            else:
                query = "UPDATE register SET password=%s WHERE email=%s"
                execute_query(query, (new_password, self.txtuser.get()))
                messagebox.showinfo("Success", "Your password has been reset, Please login with new Password!", parent=self.new_window)
                self.new_window.destroy()

if __name__ =="__main__":
    root=Tk()
    obj=Login_Window(root)
    root.mainloop()    