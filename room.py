from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox
import os



class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x600+230+207")
        self.root.configure(bg="silver")
        self.root.resizable(False,False) 

        # Get the current directory
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.images_dir = os.path.join(self.current_dir, 'images')

    # ************************variables
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_room=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_mealcost=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_totalbill=StringVar()


    # ************************Title
        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("Bookman Old Style",20,"bold"),bg="dark green",fg="white",bd=4)
        lbl_title.place(x=0,y=0,width=1295,height=40)

    # *************************img2
        try:
            img2_path = os.path.join(self.images_dir, "logo.png")
            img2 = Image.open(img2_path)
            img2 = img2.resize((100,40), Image.Resampling.LANCZOS)
            self.photoimg2 = ImageTk.PhotoImage(img2)

            labling = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
            labling.place(x=0, y=0, width=100, height=40)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load logo: {str(e)}")


    # ***********************label frame
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking Details",font=("Bookman Old Style",13,"bold"),bg="silver")
        labelframeleft.place(x=5,y=50,width=425,height=540)


        # cust contact
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact: ",font=("Sitka Heading",13,"bold"),padx=2,pady=5,bg="silver")
        lbl_cust_contact.grid(row=0,column=0,sticky=W)
        enty_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,width=18,font=("Bookman Old Style",11))
        enty_contact.grid(row=0,column=1,sticky=W)

        # Fetch data button
        btn_FetchData=Button(labelframeleft,command=self.fetch_contact,bd=2,text="Fetch Data",font=("Sitka Heading",11,"bold"),width=9,bg='dark blue',fg='white')
        btn_FetchData.place(x=325,y=5,height=28)

        # check in
        check_in_date=Label(labelframeleft,text="Check_In Date: ",font=("Sitka Heading",13,"bold"),padx=2,pady=5,bg="silver")
        check_in_date.grid(row=1,column=0,sticky=W)
        txt_check_in=ttk.Entry(labelframeleft,textvariable=self.var_checkin,width=28,font=("Bookman Old Style",11))
        txt_check_in.grid(row=1,column=1)

        # check out
        check_out_date=Label(labelframeleft,text="Check_Out Date: ",font=("Sitka Heading",13,"bold"),padx=2,pady=5,bg="silver")
        check_out_date.grid(row=2,column=0,sticky=W)
        txt_Check_out=ttk.Entry(labelframeleft,textvariable=self.var_checkout,width=28,font=("Bookman Old Style",11))
        txt_Check_out.grid(row=2,column=1)

        # Room type
        label_RoomType=Label(labelframeleft,text="Room Type: ",font=("Sitka Heading",13,"bold"),padx=2,pady=5,bg="silver")
        label_RoomType.grid(row=3,column=0,sticky=W)

        combo_RoomType = ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("Bookman Old Style",11),width=26, justify='center',state="readonly")
        combo_RoomType['values']=("Single","Double","Luxury")
        combo_RoomType.grid(row=3,column=1,sticky=W)
        combo_RoomType.current(0)

        # Available room
        lblroom=Label(labelframeleft,text="Available Room: ",font=("Sitka Heading",13,"bold"),padx=2,pady=5,bg="silver")
        lblroom.grid(row=4,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="pranjal,321",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows=my_cursor.fetchall()

        combo_RoomNo = ttk.Combobox(labelframeleft,textvariable=self.var_room,font=("Bookman Old Style",11),width=26, justify='center')
        combo_RoomNo['values']=rows
        combo_RoomNo.grid(row=4,column=1,sticky=W)
        combo_RoomNo.current(0)

        # Meal
        lbl_Meal=Label(labelframeleft,text="Meal: ",font=("Sitka Heading",13,"bold"),padx=2,pady=5,bg="silver")
        lbl_Meal.grid(row=5,column=0,sticky=W)
        txtMeal=ttk.Entry(labelframeleft,textvariable=self.var_meal,width=28,font=("Bookman Old Style",11))
        txtMeal.grid(row=5,column=1)

        # No of days
        lblNoOfDays=Label(labelframeleft,text="No Of Days: ",font=("Sitka Heading",13,"bold"),padx=2,pady=5,bg="silver")
        lblNoOfDays.grid(row=6,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_noofdays,width=28,font=("Bookman Old Style",11))
        txtNoOfDays.grid(row=6,column=1)

        # Meal Cost
        lbl_MealCost=Label(labelframeleft,text="Meal Cost: ",font=("Sitka Heading",13,"bold"),padx=2,pady=5,bg="silver")
        lbl_MealCost.grid(row=7,column=0,sticky=W)
        txtMealCost=ttk.Entry(labelframeleft,textvariable=self.var_mealcost,width=28,font=("Bookman Old Style",11))
        txtMealCost.grid(row=7,column=1)

        # Paid Tax
        lblPaidTax=Label(labelframeleft,text="Paid Tax: ",font=("Sitka Heading",13,"bold"),padx=2,pady=5,bg="silver")
        lblPaidTax.grid(row=8,column=0,sticky=W)
        txtPaidTax=ttk.Entry(labelframeleft,textvariable=self.var_paidtax,width=28,font=("Bookman Old Style",11))
        txtPaidTax.grid(row=8,column=1)

        # Sub Total
        lblSubTotal=Label(labelframeleft,text="Sub Total: ",font=("Sitka Heading",13,"bold"),padx=2,pady=5,bg="silver")
        lblSubTotal.grid(row=9,column=0,sticky=W)
        txtSubTotal=ttk.Entry(labelframeleft,textvariable=self.var_actualtotal,width=28,font=("Bookman Old Style",11))
        txtSubTotal.grid(row=9,column=1)

        # Total Cost
        lblTotalCost=Label(labelframeleft,text="Total Cost: ",font=("Sitka Heading",13,"bold"),padx=2,pady=5,bg="silver")
        lblTotalCost.grid(row=10,column=0,sticky=W)
        txtTotalCostlblTotalCost=ttk.Entry(labelframeleft,textvariable=self.var_totalbill,width=28,font=("Bookman Old Style",11))
        txtTotalCostlblTotalCost.grid(row=10,column=1)

    # ************************Bill Button************************
        btnBill=Button(labelframeleft,text='Bill',command=self.total,font=("Bookman Old Style",11,"bold"),width=10,bg='dark blue',fg='white',relief=RAISED)
        btnBill.grid(row=11,column=0,padx=5,pady=12,sticky=W)


        
    # **************************Button********************
        btn_frame=Frame(labelframeleft,bd=2)
        btn_frame.place(x=0,y=467,width=420,height=40)

        btnAdd=Button(btn_frame,text='Add',command=self.add_data,font=("Bookman Old Style",11,"bold"),width=9,bg='dark blue',fg='white')
        btnAdd.grid(row=0,column=0,padx=1.5,sticky=W)

        btnUpdate=Button(btn_frame,text='Update',command=self.update,font=("Bookman Old Style",11,"bold"),width=9,bg='dark blue',fg='white')
        btnUpdate.grid(row=0,column=1,padx=1.5,sticky=W)

        btnDelete=Button(btn_frame,text='Delete',command=self.Delete,font=("Bookman Old Style",11,"bold"),width=9,bg='dark blue',fg='white')
        btnDelete.grid(row=0,column=2,padx=1.5,sticky=W)

        btnReset=Button(btn_frame,text='Reset',command=self.Reset,font=("Bookman Old Style",11,"bold"),width=9,bg='dark blue',fg='white')
        btnReset.grid(row=0,column=3,padx=1.5,sticky=W)

    # *****************tabel frame search**********************
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details & Search System",font=("Bookman Old Style",13,"bold"),padx=2,bg="silver")
        Table_Frame.place(x=435,y=280,width=858,height=315)

        lblSearchby= Label(Table_Frame,text="Search By: ",font=("Bookman Old Style",14,"bold"),bg="red",fg="white",relief=RIDGE)
        lblSearchby.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_search = ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("Bookman Old Style",14,"bold"),width=14,state="readonly")
        combo_search['values']=("Select","Contact","Room")
        combo_search.grid(row=0,column=1,sticky=W,padx=2)
        combo_search.current(0)

        self.txt_search=StringVar()
        txtSearch = ttk.Entry(Table_Frame,textvariable=self.txt_search,font=("Bookman Old Style",14,"bold"),width=19, justify='center')
        txtSearch.grid(row=0,column=2,padx=2,sticky=W)

        btnSearch = Button(Table_Frame,text="Search",command=self.search,font=("Bookman Old Style",13,"bold"),width=10, bg="black",fg="gold")
        btnSearch.grid(row=0,column=3,padx=2,sticky=W)

        btnShowall = Button(Table_Frame,text="Show All",command=self.fetch_data,font=("Bookman Old Style",13,"bold"),width=10, bg="black",fg="gold")
        btnShowall.grid(row=0,column=4,padx=2,sticky=W)

    # *************************img1***************************************
        try:
            img1_path = os.path.join(self.images_dir, "im5.jpg")
            img1 = Image.open(img1_path)
            img1 = img1.resize((540,240), Image.Resampling.LANCZOS)
            self.photoimg1 = ImageTk.PhotoImage(img1)

            labling = Label(self.root, image=self.photoimg1)
            labling.place(x=750, y=45, width=540, height=240)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load right side image: {str(e)}")

    # ***********************Show data Table******************************

        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=40,width=851,height=250)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(details_table,column=("contact","checkin","checkout","roomtype","room","meal","noOfdays","mealcost","totalbill"), xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("checkin",text="Cheak_in")
        self.room_table.heading("checkout",text="Check_out")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("room",text="Room No")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noOfdays",text="No Of Days")
        self.room_table.heading("mealcost",text="Meal Cost")
        self.room_table.heading("totalbill",text="Total Bill")

        self.room_table["show"]="headings"

        self.room_table.column("contact",width=120)
        self.room_table.column("checkin",width=120)
        self.room_table.column("checkout",width=120)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("room",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noOfdays",width=80)
        self.room_table.column("mealcost",width=100)
        self.room_table.column("totalbill",width=120)

        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_currsor)

        self.fetch_data()


    #******************  add data
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All fields are requaired",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="pranjal,321",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                        self.var_contact.get(),
                                        self.var_checkin.get(),
                                        self.var_checkout.get(),
                                        self.var_roomtype.get(),
                                        self.var_room.get(),
                                        self.var_meal.get(),
                                        self.var_noofdays.get(),
                                        self.var_mealcost.get(),
                                        self.var_totalbill.get()
                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room Booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)

    # fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="pranjal,321",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
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

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_room.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6]),
        self.var_mealcost.set(row[7]),
        self.var_totalbill.set(row[8])


# ******update function
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please  enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="pranjal,321",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set Contact=%s, Check_in=%s, Check_out=%s, Roomtype=%s, Meal=%s, NoOfDays=%s, Meal_Cost=%s, Total_Bill=%s where Room=%s",(  
                            self.var_contact.get(),
                            self.var_checkin.get(),
                            self.var_checkout.get(),
                            self.var_roomtype.get(),
                            self.var_meal.get(),
                            self.var_noofdays.get(),
                            self.var_mealcost.get(),
                            self.var_totalbill.get(),
                            self.var_room.get()
                            
                           
                        ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been updated successfully",parent=self.root)

# *******Delete
    def Delete(self):
        Delete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer",parent=self.root) 
        if Delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="pranjal,321",database="management")
            my_cursor=conn.cursor()
            query="Delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not Delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

# *******Reset
    def Reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_room.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")
        self.var_mealcost.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_totalbill.set("")

    # *******************************All data fetch***********************
    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter Contact Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="pranjal,321",database="management")
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This message is Not Found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                # frame************************************************
                FetchDataframe=Frame(self.root,bd=2,relief=RIDGE)
                FetchDataframe.place(x=435,y=50,width=305,height=210)

                # ***********************Name***************************
                lblName=Label(FetchDataframe,text="Name:",font=("Sitka Heading",13,"bold"))
                lblName.place(x=5,y=8)
                lbl=Label(FetchDataframe,text=row,font=("Sitka Heading",13,"bold"))
                lbl.place(x=100,y=8)

                # ***************************Gender***********************
                conn=mysql.connector.connect(host="localhost",username="root",password="pranjal,321",database="management")
                my_cursor=conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(FetchDataframe,text="Gender:",font=("Sitka Heading",13,"bold"))
                lblGender.place(x=5,y=40)
                lbl2=Label(FetchDataframe,text=row,font=("Sitka Heading",13,"bold"))
                lbl2.place(x=100,y=40)

                # *************************Email*************************
                conn=mysql.connector.connect(host="localhost",username="root",password="pranjal,321",database="management")
                my_cursor=conn.cursor()
                query=("select Email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblEmail=Label(FetchDataframe,text="Email:",font=("Sitka Heading",13,"bold"))
                lblEmail.place(x=5,y=72)
                lbl3=Label(FetchDataframe,text=row,font=("Sitka Heading",13,"bold"))
                lbl3.place(x=100,y=72)

                # ****************************Nationality*****************
                conn=mysql.connector.connect(host="localhost",username="root",password="pranjal,321",database="management")
                my_cursor=conn.cursor()
                query=("select Nationality from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblNationality=Label(FetchDataframe,text="Nationality:",font=("Sitka Heading",13,"bold"))
                lblNationality.place(x=5,y=104)
                lbl4=Label(FetchDataframe,text=row,font=("Sitka Heading",13,"bold"))
                lbl4.place(x=100,y=104)

                # ***************************Address**********************
                conn=mysql.connector.connect(host="localhost",username="root",password="pranjal,321",database="management")
                my_cursor=conn.cursor()
                query=("select Address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblAddress=Label(FetchDataframe,text="Address:",font=("Sitka Heading",13,"bold"))
                lblAddress.place(x=5,y=136)
                lbl5=Label(FetchDataframe,text=row,font=("Sitka Heading",13,"bold"))
                lbl5.place(x=100,y=136)

    # ****search system
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="pranjal,321",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room where "+str(self.search_var.get())+ " LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()   

    # **********Total
    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%y/%m/%d")
        outDate=datetime.strptime(outDate,"%y/%m/%d")
        self.var_noofdays.set(abs(outDate-inDate).days)

    # Single room
        if self.var_roomtype.get()=="Single":
            q1=float(800)
            q2=float(self.var_mealcost.get())
            q3=float(self.var_noofdays.get())
            q4=float(q1*q3)
            q5=float(q4+q2)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_totalbill.set(TT)

    # Double room
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Double"):
            q1=float(1200)
            q2=float(self.var_mealcost.get())
            q3=float(self.var_noofdays.get())
            q4=float(q1*q3)
            q5=float(q4+q2)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_totalbill.set(TT)


    # Luxury room
        elif self.var_roomtype.get()=="Luxury":
            q1=float(2500)
            q2=float(self.var_mealcost.get())
            q3=float(self.var_noofdays.get())
            q4=float(q1*q3)
            q5=float(q4+q2)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_totalbill.set(TT)














if __name__ =="__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()         
