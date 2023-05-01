import tkinter as tk
import ttkbootstrap as ttkb
import main
import os
from datetime import datetime
import sys

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cheque maker")
        ico_path = os.path.join(sys._MEIPASS, 'Dhs.ico')
        self.root.iconbitmap(ico_path)
        # root geometry fullscreen
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth(),
                                                self.root.winfo_screenheight()))
        self.root.resizable(True, True)

        # background image
        bg_path = os.path.join(sys._MEIPASS, 'bg.gif')
        self.background_image = tk.PhotoImage(file=bg_path)
        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # title
        self.title = tk.Label(self.root, text="Cheque maker", font=("Helvetica", 30))
        self.title.pack(pady=(50,20))

        # label and entrys for name amount date and cause
        self.name_label = ttkb.Label(self.root, text="Nom ou dénomination", background="", borderwidth=0)
        self.name_label.place(x=200, y=350)
        self.name_entry = ttkb.Entry(self.root, font=("Helvetica", 12))
        self.name_entry.place(x=400, y=350)

        self.amount_label = ttkb.Label(self.root, text="Montant", background="", borderwidth=0)
        self.amount_label.place(x=1100, y=450)
        self.amount_entry = ttkb.Entry(self.root, font=("Helvetica", 12))
        self.amount_entry.place(x=1200, y=450)

        self.date_label = ttkb.Label(self.root, text="Date d'échéance", background="", borderwidth=0)
        self.date_label.place(x=1100, y=350)
        self.date_entry = ttkb.DateEntry(self.root)
        self.date_entry.place(x=1200, y=350)

        self.cause_label = ttkb.Label(self.root, text="Cause", background="", borderwidth=0)
        self.cause_label.place(x=200, y=550)
        self.cause_entry = ttkb.Entry(self.root, font=("Helvetica", 12))
        self.cause_entry.place(x=400, y=550)

        self.lieu_et_date_label = ttkb.Label(self.root, text="Lieu et date", background="", borderwidth=0)
        self.lieu_et_date_label.place(x=200, y=450)
        self.lieu_et_date_entry = ttkb.Entry(self.root, font=("Helvetica", 12))
        self.lieu_et_date_entry.place(x=400, y=450)
        #radio button
        def radio_button(i):
            if i ==1 or i == 3:
                print(i, "if")
                self.cause_label.place(x=200, y=550)
                self.cause_entry.place(x=400, y=550)
                self.lieu_et_date_label.configure(text="Lieu et date")
            else:
                print(i, "else")
                self.cause_label.place_forget()
                self.cause_entry.place_forget()
                self.lieu_et_date_label.configure(text="Lieu")

        self.radio_var = tk.IntVar()
        self.radio_var.set(1)
        self.radio1 = ttkb.Radiobutton(self.root, text="Cheque auto amine", variable=self.radio_var, value=1,command = lambda:radio_button(1))
        self.radio1.place(x=700, y=600)
        self.radio2 = ttkb.Radiobutton(self.root, text="Cheque Marpia", variable=self.radio_var, value=2,command =lambda: radio_button(2))
        self.radio2.place(x=1000, y=600)
        self.radio3 = ttkb.Radiobutton(self.root, text="Effet Marpia", variable=self.radio_var, value=3,command =lambda: radio_button(3))
        self.radio3.place(x=1200, y=600)

        # submit button
        def submit():

            date_str = self.date_entry.entry.get()
            date_obj = datetime.strptime(date_str, '%m/%d/%Y').date()
            formatted_date = date_obj.strftime('%d/%m/%Y')

            if self.radio_var.get() == 1:
                doc = main.check_auto_amine(self.name_entry.get(), self.amount_entry.get(),formatted_date, self.cause_entry.get(), self.lieu_et_date_entry.get())

            elif self.radio_var.get() == 2:
                doc = main.check_marpia(self.name_entry.get(), self.amount_entry.get(),formatted_date, self.lieu_et_date_entry.get())
            else:
                doc = main.effet_marpia(self.name_entry.get(), self.amount_entry.get(),formatted_date, self.lieu_et_date_entry.get(), self.cause_entry.get())
            doc.write_all()
            os.startfile("check.pdf")


        # button
        self.style = ttkb.Style("flatly")
        self.style.configure("TButton", padding=10, relief="flat")
        self.button = ttkb.Button(self.root, text="Submit",command=submit)
        self.button.pack(pady=30)

        self.root.mainloop()

GUI()