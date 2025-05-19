from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import psycopg2
import os



class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Form")
        self.root.geometry("1550x800+0+0")
        self.root.resizable(False,False) 
        # self.root.attributes('-fullscreen',True)

        # Get the current directory
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.images_dir = os.path.join(self.current_dir, 'images')

# ======variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        

    # **************img
        try:
            img_path = os.path.join(self.images_dir, "leaves.jpg")
            img = Image.open(img_path)
            img = img.resize((1550,900), Image.Resampling.LANCZOS)
            self.photoimg = ImageTk.PhotoImage(img)

            labling = Label(self.root, image=self.photoimg, bg='light yellow')
            labling.place(x=0, y=0, width=1550, height=900)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load background image: {str(e)}")

    # ***************img1
        try:
            img1_path = os.path.join(self.images_dir, "happy1.jpg")
            img1 = Image.open(img1_path)
            img1 = img1.resize((455,430), Image.Resampling.LANCZOS)
            self.photoimg1 = ImageTk.PhotoImage(img1)
            labling1 = Label(self.root, image=self.photoimg1, bg='white', relief=RAISED, borderwidth=5)
            labling1.place(x=80, y=100, width=470, height=550)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load side image: {str(e)}")


    # **************** frame
        frame=Frame(self.root,bg='white',)
        frame.place(x=550,y=100,width=800,height=550)
        
        register_lbl=Label(frame,text='REGISTER HERE',font=('times new roman',20,'bold'),fg='green',bg='white')
        register_lbl.place(x=20,y=20)

# *****************label and entry

    # -----------------row1
        fname=Label(frame,text="First Name",font=('times new roman',15,'bold'),fg='black',bg='white')
        fname.place(x=50,y=100)

        frame_entry=ttk.Entry(frame,textvariable=self.var_fname,font=('times new roman',15),)
        frame_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=('times new roman',15,'bold'),fg='black',bg='white')
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=('times new roman',15))
        self.txt_lname.place(x=370,y=130,width=250)

    # -----------------row2
        contact=Label(frame,text="Contact No",font=('times new roman',15,'bold'),fg='black',bg='white')
        contact.place(x=50,y=170)

        frame_entry = ttk.Entry(frame,textvariable=self.var_contact,font=('times new roman',15))
        frame_entry.place(x=50,y=200,width=250)

        l_name=Label(frame,text="Email",font=('times new roman',15,'bold'),fg='black',bg='white')
        l_name.place(x=370,y=170)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_email,font=('times new roman',15))
        self.txt_lname.place(x=370,y=200,width=250)

    # ------------------row3
        security_Q=Label(frame,text="Select Security Question",font=('times new roman',15,'bold'),fg='black',bg='white')
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=('times new roman',15),state='readonly')
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Pet Name","Your Favourit Place","Your Dearest Person","Your Favourite Flowers","Your Favourite Book")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer",font=('times new roman',15,'bold'),fg='black',bg='white')
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=('times new roman',15))
        self.txt_security.place(x=370,y=270,width=250)


    # ------------------row4
        pswd=Label(frame,text="Password",font=('times new roman',15,'bold'),fg='black',bg='white')
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=('times new roman',15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=('times new roman',15,'bold'),fg='black',bg='white')
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=('times new roman',15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

    # ========================checkbutton============================
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,text="I Agree The Terms & Conditions",variable=self.var_check,font=('times new roman',15,'bold'),bg='white',fg='black',onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=380)

    # ========================button=================================
        try:
            img2_path = os.path.join(self.images_dir, "register-now-button.jpg")
            img2 = Image.open(img2_path)
            img2 = img2.resize((200,60), Image.Resampling.LANCZOS)
            self.photoimage = ImageTk.PhotoImage(img2)
            b1=Button(frame,image=self.photoimage,command=self.register_data,bg='white',relief=RAISED,borderwidth=0,cursor="hand2")
            b1.place(x=60,y=420,width=200,height=60)

            img3_path = os.path.join(self.images_dir, "lgin.png")
            img3 = Image.open(img3_path)
            img3 = img3.resize((200,90), Image.Resampling.LANCZOS)
            self.photoimg3 = ImageTk.PhotoImage(img3)
            b2=Button(frame,image=self.photoimg3,command=self.return_login,bg='white',relief=RAISED,borderwidth=0,cursor="hand2")
            b2.place(x=380,y=420,width=200,height=90)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load button images: {str(e)}")

# =======================Function Declaration=========================
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password and Confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="pranjal,321",database="management")
            my_cursor=conn.cursor()
            query=("select * from register where Email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist, please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                        self.var_fname.get(),
                                        self.var_lname.get(),
                                        self.var_contact.get(),
                                        self.var_email.get(),
                                        self.var_securityQ.get(),
                                        self.var_securityA.get(),
                                        self.var_pass.get()
                                    ))
                                        
            conn.commit()
            # self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Register Successfully",parent=self.root)
    def return_login(self):
        self.root.destroy()






if __name__ =="__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()  