from tkinter import *
from tkinter import ttk, messagebox, filedialog
from db_config import execute_query
import pandas as pd

class Report:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x600+230+207")
        self.root.configure(bg="silver")
        self.root.resizable(False, False)

        lbl_title = Label(self.root, text="REPORT GENERATION", font=("Bookman Old Style", 20, "bold"),
                          bg="dark green", fg="white", bd=4)
        lbl_title.place(x=0, y=0, width=1295, height=40)

        main_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Generate Reports",
                               font=("Bookman Old Style", 12, "bold"), bg="silver")
        main_frame.place(x=5, y=50, width=1280, height=540)

        lbl_report_type = Label(main_frame, text="Report Type:", font=("Bookman Old Style", 12, "bold"), bg="silver")
        lbl_report_type.place(x=10, y=20)

        self.report_type = StringVar()
        combo_report = ttk.Combobox(main_frame, textvariable=self.report_type, font=("Bookman Old Style", 12),
                                    width=20, state="readonly")
        combo_report['values'] = ("Room Booking Report", "Room Details Report")
        combo_report.place(x=150, y=20)
        combo_report.current(0)

        lbl_from = Label(main_frame, text="From Date (YYYY-MM-DD):", font=("Bookman Old Style", 12, "bold"), bg="silver")
        lbl_from.place(x=10, y=60)
        self.from_date = StringVar()
        txt_from = ttk.Entry(main_frame, textvariable=self.from_date, font=("Bookman Old Style", 12), width=20)
        txt_from.place(x=220, y=60)

        lbl_to = Label(main_frame, text="To Date (YYYY-MM-DD):", font=("Bookman Old Style", 12, "bold"), bg="silver")
        lbl_to.place(x=400, y=60)
        self.to_date = StringVar()
        txt_to = ttk.Entry(main_frame, textvariable=self.to_date, font=("Bookman Old Style", 12), width=20)
        txt_to.place(x=600, y=60)

        btn_generate = Button(main_frame, text="Generate Report", command=self.generate_report,
                              font=("Bookman Old Style", 12, "bold"), bg="dark blue", fg="white", width=15)
        btn_generate.place(x=900, y=20)

        btn_export = Button(main_frame, text="Export to Excel", command=self.export_to_excel,
                            font=("Bookman Old Style", 12, "bold"), bg="dark blue", fg="white", width=15)
        btn_export.place(x=900, y=60)

        table_frame = Frame(main_frame, bd=2, relief=RIDGE)
        table_frame.place(x=10, y=100, width=1260, height=430)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.report_table = ttk.Treeview(table_frame, columns=(), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.report_table.xview)
        scroll_y.config(command=self.report_table.yview)
        self.report_table.pack(fill=BOTH, expand=1)

    def generate_report(self):
        try:
            self.report_table.delete(*self.report_table.get_children())
            report_type = self.report_type.get()
            if report_type == "Room Booking Report":
                self.generate_room_booking_report()
            elif report_type == "Room Details Report":
                self.generate_room_details_report()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate report: {str(e)}")

    def generate_room_booking_report(self):
        try:
            from_date = self.from_date.get().strip()
            to_date = self.to_date.get().strip()
            if from_date and to_date:
                query = """
                    SELECT Contact, Check_in, Check_out, Roomtype, Room, Meal, NoOfDays, Meal_Cost, Total_Bill, Payment_Mode
                    FROM room
                    WHERE Check_in BETWEEN %s AND %s
                """
                params = (from_date, to_date)
                rows = execute_query(query, params, fetch=True)
            else:
                query = """
                    SELECT Contact, Check_in, Check_out, Roomtype, Room, Meal, NoOfDays, Meal_Cost, Total_Bill, Payment_Mode
                    FROM room
                """
                rows = execute_query(query, fetch=True)
            columns = ("Contact", "Check_in", "Check_out", "Roomtype", "Room", "Meal", "NoOfDays", "Meal_Cost", "Total_Bill", "Payment_Mode")
            self.report_table["columns"] = columns
            for col in columns:
                self.report_table.heading(col, text=col)
                self.report_table.column(col, width=120)
            if rows:
                for row in rows:
                    self.report_table.insert("", END, values=row)
            else:
                messagebox.showinfo("Info", "No data found for the selected date range")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate room booking report: {str(e)}")

    def generate_room_details_report(self):
        try:
            query = "SELECT Floor, RoomNo, RoomType FROM details"
            rows = execute_query(query, fetch=True)
            columns = ("Floor", "RoomNo", "RoomType")
            self.report_table["columns"] = columns
            for col in columns:
                self.report_table.heading(col, text=col)
                self.report_table.column(col, width=120)
            if rows:
                for row in rows:
                    self.report_table.insert("", END, values=row)
            else:
                messagebox.showinfo("Info", "No room details found")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate room details report: {str(e)}")

    def export_to_excel(self):
        try:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".xlsx",
                filetypes=[("Excel files", "*.xlsx")],
                title="Save Report As"
            )
            if file_path:
                data = []
                for item in self.report_table.get_children():
                    data.append(self.report_table.item(item)['values'])
                df = pd.DataFrame(data, columns=self.report_table["columns"])
                df.to_excel(file_path, index=False)
                messagebox.showinfo("Success", "Report exported successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export report: {str(e)}")

if __name__ == "__main__":
    root = Tk()
    obj = Report(root)
    root.mainloop()                