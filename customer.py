from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
import os



class Cust_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1305x658+224+175")
        self.root.resizable(False,False) 

        # Get the current directory
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.images_dir = os.path.join(self.current_dir, 'images')

        # ********************variables
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_DOB=StringVar()
        self.var_Occupation=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_no=StringVar()
        self.var_address=StringVar()
        



         # ************************Title
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="white",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1305,height=45)

        # ************************img2
        try:
            img2_path = os.path.join(self.images_dir, "logo.png")
            img2 = Image.open(img2_path)
            img2 = img2.resize((100,40), Image.Resampling.LANCZOS)
            self.photoimg2 = ImageTk.PhotoImage(img2)

            labling = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
            labling.place(x=5, y=2, width=100, height=40)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load logo: {str(e)}")

        # ***********************label frame
        labelframeleft=LabelFrame(self.root,bd=4,relief=RIDGE,text="CUSTOMER DETAILS",font=("times new roman",12,"bold"))
        labelframeleft.place(x=8,y=55,width=429,height=590)

        # ***********************labels and entry
        # cust refrence
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref: ",font=("times new roman",12,"bold"),padx=2,pady=7)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        enty_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=29,font=("ariel",13,"bold"),state="readonly")
        enty_ref.grid(row=0,column=1)
        
        # cust name
        cname=Label(labelframeleft,text="Customer Name: ",font=("ariel",12,"bold"),padx=2,pady=7)
        cname.grid(row=1,column=0,sticky=W)
        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,font=("ariel",13,"bold"),width=29)
        txtcname.grid(row=1,column=1)

        # Date of birth
        lblfname=Label(labelframeleft,text="Date Of Birth: ",font=("ariel",12,"bold"),padx=2,pady=7)
        lblfname.grid(row=2,column=0,sticky=W)
        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_DOB,font=("ariel",13,"bold"),width=29)
        txtcname.grid(row=2,column=1)

        # Occupation
        lblmname=Label(labelframeleft,text="Occupation: ",font=("ariel",12,"bold"),padx=2,pady=7)
        lblmname.grid(row=3,column=0,sticky=W)
        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_Occupation,font=("ariel",13,"bold"),width=29)
        txtcname.grid(row=3,column=1)

        # gender
        label_gender=Label(labelframeleft,text="Gender: ",font=("ariel",12,"bold"),padx=2,pady=7)
        label_gender.grid(row=4,column=0,sticky=W)
        
        combo_gender = ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("ariel",12,"bold"),width=15,state="readonly")
        combo_gender['values']=("Male", "Female","Other")
        combo_gender.grid(row=4,column=1,sticky=W)
        combo_gender.current(0)

        # Postcode
        lblPostCode= Label(labelframeleft,text="PostCode: ",font=("ariel",12,"bold"),padx=2,pady=7)
        lblPostCode.grid(row=5,column=0,sticky=W)
        txtPostCode=ttk.Entry(labelframeleft,textvariable=self.var_post,font=("ariel",13,"bold"),width=15)
        txtPostCode.grid(row=5,column=1,sticky=W)


        # Contact
        lblMobile=Label(labelframeleft,text="Mobile: ",font=("ariel",12,"bold"),padx=2,pady=7)
        lblMobile.grid(row=6,column=0,sticky=W)
        txtMobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile,font=("ariel",13,"bold"),width=29)
        txtMobile.grid(row=6,column=1)

        # Email
        lblEmail= Label(labelframeleft,text="Email: ",font=("ariel",12,"bold"),padx=2,pady=7)
        lblEmail.grid(row=7,column=0,sticky=W)
        txtEmail=ttk.Entry(labelframeleft,textvariable=self.var_email,font=("ariel",13,"bold"),width=29)
        txtEmail.grid(row=7,column=1)

        # Nationality
        lblNationality= Label(labelframeleft,text="Nationality: ",font=("ariel",12,"bold"),padx=2,pady=7)
        lblNationality.grid(row=8,column=0,sticky=W)

        combo_nationality = ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("ariel",12,"bold"),width=19,state="readonly")
        combo_nationality['value']=("Select your option","Afghan","Algerian","American","Argentine","Armenian","Australian","Austrian","Azerbaijani","Bahamian","Bahraini","Bangladeshi","Belizean","Beninese","Bermudian","Bhutanese","Botswanan","Brazilian","British","British Virgin Islander","Bulgarian","Cameroonian","Canadian","Cape Verdean","Cayman Islander","Central African","Chadian","Chilean","Chinese","Citizen of Antigua and Barbuda","Citizen of Bosnia and Herzegovina","Citizen of Guinea-Bissau","Colombian","Congolese (Congo)","Cook Islander","Costa Rican","Croatian","Djiboutian","Dominican","Dutch","East Timorese","Ecuadorean","Egyptian","Emirati","English","Equatorial Guinean","Eritrean","Estonian","Ethiopian","Faroese","Fijian","Filipino","Finnish","French","Gabonese","Gambian","Georgian","German","Ghanaian","Gibraltarian","Greek","Greenlandic","Grenadian","Guamanian","Guatemalan","Guinean","Guyanese","Haitian","Honduran","Hong Konger","Hungarian","Icelandic","Indian","Indonesian","Iranian","Iraqi","Irish","Israeli","Italian","Japanese","Jordanian","Kenyan","Kuwaiti","Malaysian","Maldivian","Mexican","Nepalese","New Zealander","Nigerian","Nigerien","North Korean","Northern Irish","Norwegian","Pakistani","Portuguese","Romanian","Russian","Saudi Arabian","Scottish","Serbian","Singaporean","South African","South Korean","Spanish","Sri Lankan","Swedish","Syrian","Thai","Tunisian","Turkish","Ugandan")
        combo_nationality.grid(row=8,column=1,sticky=W)
        combo_nationality.current(0)

        # Idproof and type combobox
        lblIdProof= Label(labelframeleft,text="Id Proof Type: ",font=("ariel",12,"bold"),padx=2,pady=7)
        lblIdProof.grid(row=9,column=0,sticky=W)

        combo_Id = ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,font=("ariel",12,"bold"),width=19,state="readonly")
        combo_Id['value']=("Select your Id", "Adhar Card","Passport","Driving Licence","Voter ID")
        combo_Id.current(0)
        combo_Id.grid(row=9,column=1,sticky=W)
       
        
        # Id Number
        lblIdNumber= Label(labelframeleft,text="Id Number: ",font=("ariel",12,"bold"),padx=2,pady=7)
        lblIdNumber.grid(row=10,column=0,sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft,textvariable=self.var_id_no,font=("ariel",13,"bold"),width=29)
        txtIdNumber.grid(row=10,column=1)


        # Address
        lblAddress= Label(labelframeleft,text="Address: ",font=("ariel",12,"bold"),padx=2,pady=7)
        lblAddress.grid(row=11,column=0,sticky=W)
        txtAddress=ttk.Entry(labelframeleft,textvariable=self.var_address,font=("ariel",13,"bold"),width=29)
        txtAddress.grid(row=11,column=1,sticky=W)

         #********************** Button********************
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=5,y=500,width=412,height=40)

        btnAdd=Button(btn_frame,text='Add',command=self.add_data,font=("Sitka Heading",13,"bold"),width=9,cursor='hand2',bg='black',fg='white')
        btnAdd.grid(row=0,column=0,padx=1,sticky=W)

        btnUpdate=Button(btn_frame,text='Update',command=self.update,font=("Sitka Heading",13,"bold"),width=9,cursor='hand2',bg='black',fg='white')
        btnUpdate.grid(row=0,column=1,padx=1,sticky=W)

        btnDelete=Button(btn_frame,text='Delete',command=self.Delete,font=("Sitka Heading",13,"bold"),width=9,cursor='hand2',bg='black',fg='white')
        btnDelete.grid(row=0,column=2,padx=1,sticky=W)

        btnReset=Button(btn_frame,text='Reset',command=self.Reset,font=("Sitka Heading",13,"bold"),width=9,cursor='hand2',bg='black',fg='white')
        btnReset.grid(row=0,column=3,padx=1,sticky=W)

        # *****************tabel frame search**********************
        Table_Frame=LabelFrame(self.root,bd=4,relief=RIDGE,text="VIEW DETAILS & SEARCH SYSTEM",font=("Sitka Heading",13,"bold"),padx=2)
        Table_Frame.place(x=440,y=51,width=862,height=594)

        lblSearchby= Label(Table_Frame,text="Search By: ",font=("ariel",12,"bold"),bg="red",fg="white",relief=RIDGE)
        lblSearchby.place(x=5,y=7,width=130,height=30)

        self.search_var=StringVar()
        combo_search = ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("ariel",12,"bold"),width=13,state="readonly")
        combo_search['values']=("Ref","Mobile")
        combo_search.place(x=5,y=51,width=155,height=30)
        combo_search.current(0)

        self.txt_search=StringVar()
        txtSearch = ttk.Entry(Table_Frame,textvariable=self.txt_search,font=("Sitka Heading",13,"bold"),width=15)
        txtSearch.place(x=165,y=51,width=185,height=30)

        btnSearch = Button(Table_Frame,text="Search",command=self.search,font=("Sitka Heading",13,"bold"),width=10, bg="black",fg="white")
        btnSearch.place(x=5,y=96,height=35)

        btnShowall = Button(Table_Frame,text="Show All",command=self.fetch_data,font=("Sitka Heading",13,"bold"),width=10, bg="black",fg="white")
        btnShowall.place(x=130,y=96,height=35)

        try:
            img3_path = os.path.join(self.images_dir, "hp3.jpg")
            img3 = Image.open(img3_path)
            img3 = img3.resize((435,203), Image.Resampling.LANCZOS)
            self.photoimg3 = ImageTk.PhotoImage(img3)

            labling = Label(Table_Frame, image=self.photoimg3)
            labling.place(x=395, y=0, width=457, height=203)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load table image: {str(e)}")


        # ***********************Show data Table

        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=200,width=852,height=360)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,column=("ref","name","father","mother","gender","post","mobile","email","nationality","idproof","idnumber", "address"), xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Refer No")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("father",text="Father Name")
        self.Cust_Details_Table.heading("mother",text="Mother Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("post",text="PostCode")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="Id Proof")
        self.Cust_Details_Table.heading("idnumber",text="Id Number")
        self.Cust_Details_Table.heading("address",text="Address")

        self.Cust_Details_Table["show"]="headings"

        self.Cust_Details_Table.column("ref",width=70)
        self.Cust_Details_Table.column("name",width=110)
        self.Cust_Details_Table.column("father",width=100)
        self.Cust_Details_Table.column("mother",width=100)
        self.Cust_Details_Table.column("gender",width=80)
        self.Cust_Details_Table.column("post",width=80)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=130)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=110)
        self.Cust_Details_Table.column("address",width=160)

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_currsor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mobile.get()=="":
           messagebox.showerror("Error","All fields are requaired",parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="pranjal,321",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                        self.var_ref.get(),
                                        self.var_cust_name.get(),
                                        self.var_DOB.get(),
                                        self.var_Occupation.get(),
                                        self.var_gender.get(),
                                        self.var_post.get(),
                                        self.var_mobile.get(),
                                        self.var_email.get(),
                                        self.var_nationality.get(),
                                        self.var_id_proof.get(),
                                        self.var_id_no.get(),
                                        self.var_address.get()
                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Success","Customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="pranjal,321",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_currsor(self,event=""):
        currsor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(currsor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_DOB.set(row[2]),
        self.var_Occupation.set(row[3]),
        self.var_gender.set(row[4]),
        self.var_post.set(row[5]),
        self.var_mobile.set(row[6]),
        self.var_email.set(row[7]),
        self.var_nationality.set(row[8]),
        self.var_id_proof.set(row[9]),
        self.var_id_no.set(row[10]),
        self.var_address.set(row[11])

    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please  enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="pranjal,321",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set Name=%s, DOB=%s, Occupation=%s, Gender=%s, PostCode=%s, Mobile=%s, Email=%s, Nationality=%s, Idproof=%s, IdNumber=%s, Address=%s where Ref=%s",(  
                                        self.var_cust_name.get(),
                                        self.var_DOB.get(),
                                        self.var_Occupation.get(),
                                        self.var_gender.get(),
                                        self.var_post.get(),
                                        self.var_mobile.get(),
                                        self.var_email.get(),
                                        self.var_nationality.get(),
                                        self.var_id_proof.get(),
                                        self.var_id_no.get(),
                                        self.var_address.get(),
                                        self.var_ref.get()
                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details has been updated successfully",parent=self.root)


    def Delete(self):
        Delete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer",parent=self.root) 
        if Delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="pranjal,321",database="management")
            my_cursor=conn.cursor()
            query="Delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not Delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def Reset(self):
        # self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_DOB.set(""),
        self.var_Occupation.set(""),
        self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        self.var_nationality.set(""),
        self.var_id_proof.set(""),
        self.var_id_no.set(""),
        self.var_address.set("")

        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="pranjal,321",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer where "+str(self.search_var.get())+ " LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()   





if __name__ =="__main__":
    root=Tk()
    obj=Cust_win(root)
    root.mainloop()                