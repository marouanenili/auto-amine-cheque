import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttkb

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Title")

        # root geometry fullscreen
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth(),
                                                self.root.winfo_screenheight()))
        self.root.resizable(True, True)

        # background image
        self.background_image = tk.PhotoImage(file="bg.gif")
        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # title
        self.title = tk.Label(self.root, text="Auto Amine Cheque", font=("Helvetica", 30))
        self.title.pack(pady=(50,20))

        # label and entrys for name amount date and cause
        self.name_label = ttkb.Label(self.root, text="Nom ou dénomination", background="", borderwidth=0)
        self.name_label.place(x=200, y=350)
        self.name_entry = ttkb.Entry(self.root, font=("Helvetica", 20))
        self.name_entry.place(x=400, y=350)

        self.amount_label = ttkb.Label(self.root, text="Montant", background="", borderwidth=0)
        self.amount_label.place(x=1100, y=450)
        self.amount_entry = ttkb.Entry(self.root, font=("Helvetica", 20))
        self.amount_entry.place(x=1200, y=450)

        self.date_label = ttkb.Label(self.root, text="Date d'échéance", background="", borderwidth=0)
        self.date_label.place(x=1100, y=350)
        self.date_entry = ttkb.DateEntry(self.root)
        self.date_entry.place(x=1200, y=350)

        self.cause_label = ttkb.Label(self.root, text="Cause", background="", borderwidth=0)
        self.cause_label.place(x=200, y=450)
        self.cause_entry = ttkb.Entry(self.root, font=("Helvetica", 20))
        self.cause_entry.place(x=400, y=450)

        self.lieu_et_date_label = ttkb.Label(self.root, text="Lieu et date", background="", borderwidth=0)
        self.lieu_et_date_label.place(x=200, y=550)
        self.lieu_et_date_entry = ttkb.Entry(self.root, font=("Helvetica", 20))
        self.lieu_et_date_entry.place(x=400, y=550)

        # button
        self.style = ttkb.Style("flatly")
        self.style.configure("TButton", padding=10, relief="flat")
        self.button = ttkb.Button(self.root, text="Submit")
        self.button.pack(pady=30)

        self.root.mainloop()

GUI()