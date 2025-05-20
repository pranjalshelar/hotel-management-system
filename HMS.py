from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
from customer import Cust_win
from room import Roombooking
from details import DetailsRoom
from report import Report
import os


class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")
        self.root.attributes('-fullscreen',True)
        self.root.configure(bg="black")

        # Get the current directory
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.images_dir = os.path.join(self.current_dir, 'images')

        # **************img1
        try:
            img1_path = os.path.join(self.images_dir, "hms2.png")
            img1 = Image.open(img1_path)
            img1 = img1.resize((1315,175), Image.Resampling.LANCZOS)
            self.photoimg1 = ImageTk.PhotoImage(img1)

            labling = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
            labling.place(x=230, y=0, width=1315, height=175)
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

        # *****************Frame
        main_frame = Frame(self.root)
        main_frame.place(x=0, y=175, width=1550, height=700)
     
        # *****************main img
        try:
            img3_path = os.path.join(self.images_dir, "im3.jpg")
            img3 = Image.open(img3_path)
            img3 = img3.resize((1550,700), Image.Resampling.LANCZOS)
            self.photoimg3 = ImageTk.PhotoImage(img3)

            labling = Label(main_frame, image=self.photoimg3, relief=RIDGE)
            labling.place(x=0, y=0, width=1550, height=700)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load background image: {str(e)}")

        # ******************Buttons
        cust_button = Button(main_frame, text="CUSTOMER", command=self.cust_details, 
                           font=("Bookman Old Style",14,"bold"), bg="black", fg="white", 
                           relief=RIDGE, cursor="hand2")
        cust_button.place(x=30, y=35, width=180, height=45)

        room_button = Button(main_frame, text="ROOM", command=self.roombooking, 
                           font=("Bookman Old Style",14,"bold"), bg="black", fg="white", 
                           relief=RIDGE, cursor="hand2")
        room_button.place(x=30, y=100, width=180, height=45)

        details_button = Button(main_frame, text="DETAILS", command=self.details_room, 
                              font=("Bookman Old Style",14,"bold"), bg="black", fg="white", 
                              relief=RIDGE, cursor="hand2")
        details_button.place(x=30, y=165, width=180, height=45)

        report_button = Button(main_frame, text="REPORT", command=self.report_window, 
                             font=("Bookman Old Style",14,"bold"), bg="black", fg="white", 
                             relief=RIDGE, cursor="hand2")
        report_button.place(x=30, y=230, width=180, height=45)
        
        logout_button = Button(main_frame, text="LOGOUT", command=self.logout, 
                             font=("Bookman Old Style",14,"bold"), bg="black", fg="white", 
                             relief=RIDGE, cursor="hand2")
        logout_button.place(x=30, y=295, width=180, height=45)

    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_win(self.new_window)

    def roombooking(self):
        self.new_window = Toplevel(self.root)
        self.app = Roombooking(self.new_window)

    def details_room(self):
        self.new_window = Toplevel(self.root)
        self.app = DetailsRoom(self.new_window)

    def report_window(self):
        try:
            self.new_window = Toplevel(self.root)
            self.app = Report(self.new_window)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open report window: {str(e)}")

    def logout(self):
        if messagebox.askyesno("Logout", "Do you want to logout?", parent=self.root):
            self.root.quit()
            self.root.destroy()

if __name__ =="__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()        