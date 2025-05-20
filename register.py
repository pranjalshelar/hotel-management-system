from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
from db_config import get_db_connection

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Form")
        self.root.geometry("1550x800+0+0")
        self.root.resizable(False, False)

        # Get the current directory
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.images_dir = os.path.join(self.current_dir, 'images')

        # Variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # Load images
        try:
            img_path = os.path.join(self.images_dir, "leaves.jpg")
            img = Image.open(img_path)
            img = img.resize((1550, 900), Image.Resampling.LANCZOS)
            self.photoimg = ImageTk.PhotoImage(img)
            Label(self.root, image=self.photoimg, bg='light yellow').place(x=0, y=0, width=1550, height=900)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load background image: {str(e)}")
        try:
            img1_path = os.path.join(self.images_dir, "happy1.jpg")
            img1 = Image.open(img1_path)
            img1 = img1.resize((455, 430), Image.Resampling.LANCZOS)
            self.photoimg1 = ImageTk.PhotoImage(img1)
            Label(self.root, image=self.photoimg1, bg='white', relief=RAISED, borderwidth=5).place(x=80, y=100, width=470, height=550)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load side image: {str(e)}")

        # Registration frame
        frame = Frame(self.root, bg='white')
        frame.place(x=550, y=100, width=800, height=550)
        Label(frame, text='REGISTER HERE', font=('times new roman', 20, 'bold'), fg='green', bg='white').place(x=20, y=20)

        # Form fields
        Label(frame, text="First Name", font=('times new roman', 15, 'bold'), fg='black', bg='white').place(x=50, y=100)
        ttk.Entry(frame, textvariable=self.var_fname, font=('times new roman', 15)).place(x=50, y=130, width=250)
        Label(frame, text="Last Name", font=('times new roman', 15, 'bold'), fg='black', bg='white').place(x=370, y=100)
        ttk.Entry(frame, textvariable=self.var_lname, font=('times new roman', 15)).place(x=370, y=130, width=250)
        Label(frame, text="Contact No", font=('times new roman', 15, 'bold'), fg='black', bg='white').place(x=50, y=170)
        ttk.Entry(frame, textvariable=self.var_contact, font=('times new roman', 15)).place(x=50, y=200, width=250)
        Label(frame, text="Email", font=('times new roman', 15, 'bold'), fg='black', bg='white').place(x=370, y=170)
        ttk.Entry(frame, textvariable=self.var_email, font=('times new roman', 15)).place(x=370, y=200, width=250)
        Label(frame, text="Select Security Question", font=('times new roman', 15, 'bold'), fg='black', bg='white').place(x=50, y=240)
        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=('times new roman', 15), state='readonly')
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Pet Name", "Your Favourit Place", "Your Dearest Person", "Your Favourite Flowers", "Your Favourite Book")
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)
        Label(frame, text="Security Answer", font=('times new roman', 15, 'bold'), fg='black', bg='white').place(x=370, y=240)
        ttk.Entry(frame, textvariable=self.var_securityA, font=('times new roman', 15)).place(x=370, y=270, width=250)
        Label(frame, text="Password", font=('times new roman', 15, 'bold'), fg='black', bg='white').place(x=50, y=310)
        ttk.Entry(frame, textvariable=self.var_pass, font=('times new roman', 15)).place(x=50, y=340, width=250)
        Label(frame, text="Confirm Password", font=('times new roman', 15, 'bold'), fg='black', bg='white').place(x=370, y=310)
        ttk.Entry(frame, textvariable=self.var_confpass, font=('times new roman', 15)).place(x=370, y=340, width=250)
        self.var_check = IntVar()
        Checkbutton(frame, text="I Agree The Terms & Conditions", variable=self.var_check, font=('times new roman', 15, 'bold'), bg='white', fg='black', onvalue=1, offvalue=0).place(x=50, y=380)
        # Buttons
        try:
            img2_path = os.path.join(self.images_dir, "register-now-button.jpg")
            img2 = Image.open(img2_path)
            img2 = img2.resize((200, 60), Image.Resampling.LANCZOS)
            self.photoimage = ImageTk.PhotoImage(img2)
            Button(frame, image=self.photoimage, command=self.register_data, bg='white', relief=RAISED, borderwidth=0, cursor="hand2").place(x=60, y=420, width=200, height=60)
            img3_path = os.path.join(self.images_dir, "lgin.png")
            img3 = Image.open(img3_path)
            img3 = img3.resize((200, 90), Image.Resampling.LANCZOS)
            self.photoimg3 = ImageTk.PhotoImage(img3)
            Button(frame, image=self.photoimg3, command=self.return_login, bg='white', relief=RAISED, borderwidth=0, cursor="hand2").place(x=380, y=420, width=200, height=90)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load button images: {str(e)}")

    def register_data(self):
        """Register a new user after validating all fields."""
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password and Confirm password must be same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to our terms and conditions")
        else:
            conn = get_db_connection()
            if conn:
                try:
                    with conn.cursor() as cursor:
                        cursor.execute("SELECT * FROM register WHERE Email = %s", (self.var_email.get(),))
                        row = cursor.fetchone()
                        if row is not None:
                            messagebox.showerror("Error", "User already exists, please try another email")
                        else:
                            cursor.execute(
                                "INSERT INTO register (Fname, Lname, Contact, Email, SecurityQ, SecurityA, Password) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                                (
                                    self.var_fname.get(),
                                    self.var_lname.get(),
                                    self.var_contact.get(),
                                    self.var_email.get(),
                                    self.var_securityQ.get(),
                                    self.var_securityA.get(),
                                    self.var_pass.get()
                                )
                            )
                            conn.commit()
                            messagebox.showinfo("Success", "Registered Successfully", parent=self.root)
                except Exception as e:
                    messagebox.showerror("Error", f"Database error: {str(e)}")
                finally:
                    conn.close()

    def return_login(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()  