from tkinter import*
from PIL import Image,ImageTk
from customer import Cust_win
from room import Roombooking
import os


class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")
        self.root.resizable(False,False) 
        # self.root.attributes('-fullscreen',True)
        # self.root.configure(bg="black")

        # Get the current directory
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.images_dir = os.path.join(self.current_dir, 'images')

        # **************img1
        try:
            img1_path = os.path.join(self.images_dir, "hms2.png")
            img1 = Image.open(img1_path)
            img1 = img1.resize((1550,145), Image.Resampling.LANCZOS)
            self.photoimg1 = ImageTk.PhotoImage(img1)

            labling = Label(self.root, image=self.photoimg1, bd=4)
            labling.place(x=0, y=0, width=1550, height=145)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load header image: {str(e)}")

        # ***************img2(logo)
        try:
            img2_path = os.path.join(self.images_dir, "logo.png")
            img2 = Image.open(img2_path)
            img2 = img2.resize((230,145), Image.Resampling.LANCZOS)
            self.photoimg2 = ImageTk.PhotoImage(img2)

            labling = Label(self.root, image=self.photoimg2, bd=4)
            labling.place(x=0, y=0, width=230, height=145)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load logo: {str(e)}")

        # ****************Title
        lbl_title = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", 
                         font=("Bookman Old Style",30,"bold"), bg="black", fg="white", bd=4)
        lbl_title.place(x=0, y=145, width=1550, height=50)

        # *****************Frame
        main_frame = Frame(self.root, bd=4)
        main_frame.place(x=0, y=195, width=1550, height=620)

        # *****************Menu
        lbl_menu = Label(main_frame, text="MENU", font=("times new roman",20,"bold"),
                        bg="black", fg="gold", bd=4)
        lbl_menu.place(x=0, y=0, width=230)

        # ******************Button
        btn_frame = Frame(main_frame, bd=4)
        btn_frame.place(x=0, y=35, width=228, height=190)

        cust_button = Button(btn_frame, text="CUSTOMER", command=self.cust_details,
                           width=22, font=("times new roman",14,"bold"), bg="black",
                           fg="gold", bd=0, cursor="hand1")
        cust_button.grid(row=0, column=0, padx=0, pady=1)

        room_button = Button(btn_frame, text="ROOM", command=self.roombooking,
                           width=22, font=("times new roman",14,"bold"), bg="black",
                           fg="gold", bd=0, cursor="hand1")
        room_button.grid(row=1, column=0, padx=0, pady=1)

        details_button = Button(btn_frame, text="DETAILS", width=22,
                              font=("times new roman",14,"bold"), bg="black", fg="gold",
                              bd=0, cursor="hand1")
        details_button.grid(row=2, column=0, padx=0, pady=1)

        report_button = Button(btn_frame, text="REPORT", width=22,
                             font=("times new roman",14,"bold"), bg="black", fg="gold",
                             bd=0, cursor="hand1")
        report_button.grid(row=3, column=0, padx=0, pady=1)
        
        logout_button = Button(btn_frame, text="LOGOUT", width=22,
                             font=("times new roman",14,"bold"), bg="black", fg="gold",
                             bd=0, cursor="hand1")
        logout_button.grid(row=4, column=0, padx=0, pady=1)

        # *****************right type img
        try:
            img3_path = os.path.join(self.images_dir, "im3.jpg")
            img3 = Image.open(img3_path)
            img3 = img3.resize((1310,650), Image.Resampling.LANCZOS)
            self.photoimg3 = ImageTk.PhotoImage(img3)

            labling = Label(main_frame, image=self.photoimg3, bd=4)
            labling.place(x=225, y=0, width=1310, height=650)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load main image: {str(e)}")

        # ******************down img
        try:
            img4_path = os.path.join(self.images_dir, "h11.jpg")
            img4 = Image.open(img4_path)
            img4 = img4.resize((230,195), Image.Resampling.LANCZOS)
            self.photoimg4 = ImageTk.PhotoImage(img4)

            labling = Label(main_frame, image=self.photoimg4, bd=4)
            labling.place(x=0, y=225, width=230, height=195)

            img5_path = os.path.join(self.images_dir, "hotel2.jpg")
            img5 = Image.open(img5_path)
            img5 = img5.resize((230,190), Image.Resampling.LANCZOS)
            self.photoimg5 = ImageTk.PhotoImage(img5)

            labling = Label(main_frame, image=self.photoimg5, bd=4)
            labling.place(x=0, y=420, width=230, height=190)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load side images: {str(e)}")

    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_win(self.new_window)

    def roombooking(self):
        self.new_window = Toplevel(self.root)
        self.app = Roombooking(self.new_window)

if __name__ =="__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()        