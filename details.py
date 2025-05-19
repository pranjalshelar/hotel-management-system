from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox
import os




class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x600+230+207")
        self.root.configure(bg="silver")
        self.root.resizable(False,False) 

        # Get the current directory
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.images_dir = os.path.join(self.current_dir, 'images')

    # ************************Title
        lbl_title=Label(self.root,text="ROOM ADDING DEPARTMENT",font=("Bookman Old Style",20,"bold"),bg="dark green",fg="white",bd=4)
        lbl_title.place(x=0,y=0,width=1295,height=40)

    # ************************logo
        try:
            img2_path = os.path.join(self.images_dir, "logo.png")
            img2 = Image.open(img2_path)
            img2 = img2.resize((101,40), Image.Resampling.LANCZOS)
            self.photoimg2 = ImageTk.PhotoImage(img2)

            labling2 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
            labling2.place(x=0, y=0, width=101, height=40)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load logo: {str(e)}")

    # *********************right side image
        try:
            img1_path = os.path.join(self.images_dir, "h8.jpg")
            img1 = Image.open(img1_path)
            img1 = img1.resize((309,250), Image.Resampling.LANCZOS)
            self.photoimg1 = ImageTk.PhotoImage(img1)

            labling = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
            labling.place(x=984, y=56, width=309, height=250)

            img3_path = os.path.join(self.images_dir, "h5.jpg")
            img3 = Image.open(img3_path)
            img3 = img3.resize((309,284), Image.Resampling.LANCZOS)
            self.photoimg3 = ImageTk.PhotoImage(img3)

            labling = Label(self.root, image=self.photoimg3, bd=4, relief=RIDGE)
            labling.place(x=984, y=312, width=309, height=284)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load side images: {str(e)}")

    # ************************down img
        try:
            img4_path = os.path.join(self.images_dir, "im7.jpg")
            img4 = Image.open(img4_path)
            img4 = img4.resize((491,346), Image.Resampling.LANCZOS)
            self.photoimg4 = ImageTk.PhotoImage(img4)

            labling4 = Label(self.root, image=self.photoimg4, bd=4, relief=RIDGE)
            labling4.place(x=0, y=56, width=491, height=346)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load bottom image: {str(e)}")


    # ***********************label frame
        labelframeleft=LabelFrame(self.root,bd=2,relief=RAISED,text="Add New Room",font=("Bookman Old Style",14,"bold"),bg="silver")
        labelframeleft.place(x=8,y=47,width=480,height=200)

        # Floor
        lbl_floor=Label(labelframeleft,text="Floor: ",font=("Sitka Heading",13,"bold"),padx=2,pady=5,bg="silver")
        lbl_floor.place(x=8,y=6)

        self.var_Floor=StringVar()
        enty_floor=ttk.Entry(labelframeleft,textvariable=self.var_Floor,width=18,font=("Bookman Old Style",11))
        enty_floor.place(x=130,y=6,height=30)

        # Room No
        lbl_RoomNo=Label(labelframeleft,text="Room No: ",font=("Sitka Heading",13,"bold"),padx=2,pady=5,bg="silver")
        lbl_RoomNo.place(x=8,y=51)

        self.var_RoomNo=StringVar()
        enty_RoomNo=ttk.Entry(labelframeleft,textvariable=self.var_RoomNo,width=18,font=("Bookman Old Style",11))
        enty_RoomNo.place(x=130,y=53,height=30)

        # Room Type
        lbl_RoomType=Label(labelframeleft,text="Room Type: ",font=("Sitka Heading",13,"bold"),padx=2,pady=5,bg="silver")
        lbl_RoomType.place(x=8,y=98)

        self.var_RoomType=StringVar()
        combo_RoomType = ttk.Combobox(labelframeleft,textvariable=self.var_RoomType,font=("Sitka Heading",13),width=16,state="readonly")
        combo_RoomType['values']=("Single", "Double","Luxury")
        combo_RoomType.place(x=130,y=100)
        combo_RoomType.current(0)

        # **************************Button********************
        btn_frame=Frame(labelframeleft,bd=2,bg="silver")
        btn_frame.place(x=340,y=5,width=118,height=150)

        btnAdd=Button(btn_frame,text='Add',command=self.add_data,font=("Bookman Old Style",11,"bold"),width=10,bg='dark blue',fg='white')
        btnAdd.grid(row=0,column=0,padx=2,pady=2,sticky=W)

        btnUpdate=Button(btn_frame,text='Update',command=self.update,font=("Bookman Old Style",11,"bold"),width=10,bg='dark blue',fg='white')
        btnUpdate.grid(row=1,column=0,padx=2,pady=2,sticky=W)

        btnDelete=Button(btn_frame,text='Delete',command=self.Delete,font=("Bookman Old Style",11,"bold"),width=10,bg='dark blue',fg='white')
        btnDelete.grid(row=2,column=0,padx=2,pady=2,sticky=W)

        btnReset=Button(btn_frame,text='Reset',command=self.Reset,font=("Bookman Old Style",11,"bold"),width=10,bg='dark blue',fg='white')
        btnReset.grid(row=3,column=0,padx=2,pady=2,sticky=W)

    # room details frame*************
        Table_Frame=LabelFrame(self.root,bd=2,relief=RAISED,text="Show Room Details",font=("Bookman Old Style",14,"bold"),padx=2,bg="silver")
        Table_Frame.place(x=500,y=47,width=480,height=549)

        scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)

        self.room_table=ttk.Treeview(Table_Frame,column=("floor","roomno","roomtype"), yscrollcommand=scroll_y.set)

        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor",text="Floor")
        self.room_table.heading("roomno",text="Room No")
        self.room_table.heading("roomtype",text="Room Type")

        self.room_table["show"]="headings"

        self.room_table.column("floor",width=100)
        self.room_table.column("roomno",width=100)
        self.room_table.column("roomtype",width=100)

        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_currsor)
        self.fetch_data()

# ******************  add data
    def add_data(self):
        if self.var_Floor.get()=="" or self.var_RoomType.get()=="":
            messagebox.showerror("Error","All fields are requaired",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="pranjal,321",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(
                                        self.var_Floor.get(),
                                        self.var_RoomNo.get(),
                                        self.var_RoomType.get()
                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","New Room added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)


    # # fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="pranjal,321",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()


        
    def get_currsor(self,event=""):
        currsor_row=self.room_table.focus()
        content=self.room_table.item(currsor_row)
        row=content["values"]

        self.var_Floor.set(row[0]),
        self.var_RoomNo.set(row[1]),
        self.var_RoomType.set(row[2])
        



# ******update function
    def update(self):
        if self.var_Floor.get()=="":
            messagebox.showerror("Error","Please  enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="pranjal,321",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set Floor=%s, RoomType=%s where RoomNo=%s",(  
                            self.var_Floor.get(),
                            self.var_RoomType.get(),
                            self.var_RoomNo.get()
                        ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","New Room details has been updated successfully",parent=self.root)

# *******Delete
    def Delete(self):
        Delete=messagebox.askyesno("Hotel Management System","Do you want to delete this Room",parent=self.root) 
        if Delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="pranjal,321",database="management")
            my_cursor=conn.cursor()
            query="Delete from details where RoomNo=%s"
            value=(self.var_RoomNo.get(),)
            my_cursor.execute(query,value)
        else:
            if not Delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    # *******Reset
    def Reset(self):
        
        self.var_Floor.set("")
        self.var_RoomNo.set("")
        self.var_RoomType.set("")
       




if __name__ =="__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()         
