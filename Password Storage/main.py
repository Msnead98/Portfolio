import customtkinter
from databse import *
from passwordgen import *
import tkinter as tk
from tkinter import ttk
import sqlite3

LARGEFONT = ("Raleway", 50)
small_font = ("Raleway", 25)

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")


class App(customtkinter.CTk):

    def __init__(self):
        customtkinter.CTk.__init__(self)
        self.geometry(f"{980}x{410}")

        container = customtkinter.CTkFrame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        # Move Frames like pages
        for F in (StartPage, Add, View, Modify):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky=tk.NSEW)
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(customtkinter.CTkFrame):
    def __init__(self, parent, contr):
        customtkinter.CTkFrame.__init__(self, parent)

        label = customtkinter.CTkLabel(self, text="Safe Pass", font=LARGEFONT)

        label.place(x=350, y=150)
        label2 = customtkinter.CTkLabel(self, text="For all your password storage needs", font=small_font)
        label2.place(x=260, y=260)

        # Frame for NAV buttons
        self.nav_button = customtkinter.CTkFrame(self)
        self.nav_button.grid(row=0, column=0)

        button1 = customtkinter.CTkButton(self.nav_button, text="Add", command=lambda: contr.show_frame(Add))
        button1.grid(row=1, column=0, padx=10, pady=10)
        button2 = customtkinter.CTkButton(self.nav_button, text="View", command=lambda: contr.show_frame(View))
        button2.grid(row=2, column=0, padx=10, pady=10)
        button3 = customtkinter.CTkButton(self.nav_button, text="Modify", command=lambda: contr.show_frame(Modify))
        button3.grid(row=3, column=0, padx=10, pady=10)


class Add(customtkinter.CTkFrame):

    def __init__(self, parent, contr):
        customtkinter.CTkFrame.__init__(self, parent)
        #Frame for Account labels
        self.ad_frame = customtkinter.CTkFrame(self, width=500, height=300, corner_radius=0)
        self.ad_frame.place(x=250, y=100)

        # Frame for NAV buttons
        self.nav_button = customtkinter.CTkFrame(self)
        self.nav_button.grid(row=0, column=0)

        button1 = customtkinter.CTkButton(self.nav_button, text="View", command=lambda: contr.show_frame(View))
        button1.grid(row=1, column=0, padx=10, pady=10)
        button2 = customtkinter.CTkButton(self.nav_button, text="Modify", command=lambda: contr.show_frame(Modify))
        button2.grid(row=2, column=0, padx=10, pady=10)
        button3 = customtkinter.CTkButton(self.nav_button, text="Start Page",command=lambda: contr.show_frame(StartPage))
        button3.grid(row=3, column=0, padx=10, pady=10)

        self.passwordlen_label = customtkinter.CTkLabel(self.ad_frame, text='How long would you like the password to be?')
        self.passwordlen_label.place(x=0, y=10)

        self.passwordlen_entry = customtkinter.CTkEntry(self.ad_frame)
        self.passwordlen_entry.place(x=300, y=10)

        self.sym_label = customtkinter.CTkLabel(self.ad_frame, text='Would you like symbols?')
        self.sym_label.place(x=0, y=50)

        self.radio = tk.IntVar()
        self.rd1 = customtkinter.CTkRadioButton(self.ad_frame, variable=self.radio, text='Yes', value=0)
        self.rd2 = customtkinter.CTkRadioButton(self.ad_frame, variable=self.radio, text='No', value=1)
        self.rd1.place(x=200, y=50)
        self.rd2.place(x=300, y=50)

        self.acc_label = customtkinter.CTkLabel(self.ad_frame, text='Account')
        self.acc_label.place(x=0, y=100)

        self.acc_entry = customtkinter.CTkEntry(self.ad_frame)
        self.acc_entry.place(x=300, y=100)

        self.em_label = customtkinter.CTkLabel(self.ad_frame, text='Email or Username')
        self.em_label.place(x=0, y=150)

        self.e_entry = customtkinter.CTkEntry(self.ad_frame)
        self.e_entry.place(x=300, y=150)

        def enterstuff():
            "Takes entry box infomation and gives you a password an saves it"
            radio = self.radio.get()
            acc = self.acc_entry.get()
            em = self.e_entry.get()

            #Gets a True or False value from the radio buttons
            flag = radiobuttonconvert(radio)
            number = self.passwordlen_entry.get()
            int_answer = int(number)
            finalpass = password(int_answer, flag)
            passwordfin = finalpass
            addinfo(acc, em, passwordfin)

            self.r_lb = customtkinter.CTkLabel(self, text="Your new password is:")
            self.r_lb.place(x=400, y=50)

            self.result_lb = customtkinter.CTkLabel(self, text=finalpass)
            self.result_lb.place(x=450, y=70)

            reset()

        self.btnnext = customtkinter.CTkButton(self.ad_frame, text="Next", command=enterstuff)
        self.btnnext.place(x=170, y=200)

        def reset():
            "Clears all the entry boxes"
            self.acc_entry.delete(0, "end")
            self.passwordlen_entry.delete(0, "end")
            self.e_entry.delete(0, "end")


class View(customtkinter.CTkFrame):
    def __init__(self, parent, contr):
        customtkinter.CTkFrame.__init__(self, parent)

        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")

        button1 = customtkinter.CTkButton(self.sidebar_frame, text="Modify", command=lambda: contr.show_frame(Modify))
        button1.grid(row=1, column=0, padx=10, pady=10)
        button2 = customtkinter.CTkButton(self.sidebar_frame, text="Start Page",command=lambda: contr.show_frame(StartPage))
        button2.grid(row=2, column=0, padx=10, pady=10)
        button3 = customtkinter.CTkButton(self.sidebar_frame, text="Add", command=lambda: contr.show_frame(Add))
        button3.grid(row=3, column=0, padx=10, pady=10)

        tree = ttk.Treeview(self, columns=("Account", "Email", "Password"), show='headings')
        tree.heading("#1", text="Account")
        tree.heading("#2", text="Email")
        tree.heading("#3", text="Password")

        conn = sqlite3.connect("password.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM userinfo ORDER BY rowid DESC;")
        rows = cur.fetchall()
        for row in rows:
            tree.insert("", tk.END, values=row)
            conn.close()
        tree.grid(row=5, column=7)

        def refresh():
            "Updates treeview table by destorying and showing any new entries"
            tree.destroy()
            tree1 = ttk.Treeview(self, columns=("Account", "Email", "Password"), show='headings')
            tree1.heading("#1", text="Account")
            tree1.heading("#2", text="Email")
            tree1.heading("#3", text="Password")
            conn = sqlite3.connect("password.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM userinfo ORDER BY rowid DESC;")
            rows = cur.fetchall()
            for row in rows:
                tree1.insert("", tk.END, values=row)
                conn.close()
            tree1.grid(row=4, column=7)

        btnref = customtkinter.CTkButton(self, text="Refresh", command=refresh)
        btnref.place(x=400, y=360)


class Modify(customtkinter.CTkFrame):
    def __init__(self, parent, contr):
        customtkinter.CTkFrame.__init__(self, parent)
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")

        button1 = customtkinter.CTkButton(self.sidebar_frame, text="Start Page",command=lambda: contr.show_frame(StartPage))
        button1.grid(row=1, column=0, padx=10, pady=10)
        button2 = customtkinter.CTkButton(self.sidebar_frame, text="Add", command=lambda: contr.show_frame(Add))
        button2.grid(row=2, column=0, padx=10, pady=10)
        button3 = customtkinter.CTkButton(self.sidebar_frame, text="View", command=lambda: contr.show_frame(View))
        button3.grid(row=3, column=0, padx=10, pady=10)

        tree = ttk.Treeview(self, columns=("Account", "Email", "Password"), show='headings')
        tree.heading("#1", text="Account")
        tree.heading("#2", text="Email")
        tree.heading("#3", text="Password")
        conn = sqlite3.connect("password.db")
        cur = conn.cursor()
        cur.execute("SELECT account,email,password,rowid FROM userinfo ORDER BY rowid DESC;")
        rows = cur.fetchall()
        for row in rows:
            tree.insert("", tk.END, values=row)
            conn.close()
        tree.grid(row=4, column=2)

        self.button_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.button_frame.grid(row=4, column=4, rowspan=4, sticky="nsew")

        label_acc = customtkinter.CTkLabel(self.button_frame, text='Account')
        entry_acc = customtkinter.CTkEntry(self.button_frame)

        label_email = customtkinter.CTkLabel(self.button_frame, text='Email')
        entry_email = customtkinter.CTkEntry(self.button_frame)

        label_pass = customtkinter.CTkLabel(self.button_frame, text='Password')
        entry_pass = customtkinter.CTkEntry(self.button_frame)
        #Holds the id number for the sql query
        entry_id = customtkinter.CTkEntry(self)

        def delein():
            "Deletes enteries"
            idr = entry_id.get()
            tree.destroy()
            deleteRecord(idr)

            tree2 = ttk.Treeview(self, columns=("Account", "Email", "Password"), show='headings')
            tree2.heading("#1", text="Account")
            tree2.heading("#2", text="Email")
            tree2.heading("#3", text="Password")
            conn = sqlite3.connect("password.db")
            cur = conn.cursor()
            cur.execute("SELECT account,email,password,rowid FROM userinfo ORDER BY rowid DESC;")
            rows = cur.fetchall()
            for row in rows:
                tree2.insert("", tk.END, values=row)
                conn.close()
            tree2.grid(row=4, column=2)

            def displaySelectedItem(a):
                # clear entries
                entry_acc.delete(0, tk.END)
                entry_email.delete(0, tk.END)
                entry_pass.delete(0, tk.END)
                entry_id.delete(0, tk.END)

                selectedItem = tree2.selection()[0]
                entry_acc.insert(0, tree2.item(selectedItem)['values'][0])
                entry_email.insert(0, tree2.item(selectedItem)['values'][1])
                entry_pass.insert(0, tree2.item(selectedItem)['values'][2])
                entry_id.insert(0, tree2.item(selectedItem)['values'][3])

            tree2.bind("<<TreeviewSelect>>", displaySelectedItem)

        def edit():
            "Edits entries "
            acc = entry_acc.get()
            email = entry_email.get()
            passw = entry_pass.get()
            idr = entry_id.get()

            updateSqliteTable(update1=email, update2=passw, acc=acc, idr=idr)
            entry_acc.delete(0, tk.END)
            entry_email.delete(0, tk.END)
            entry_pass.delete(0, tk.END)
            entry_id.delete(0, tk.END)

            tree1 = ttk.Treeview(self, columns=("Account", "Email", "Password"), show='headings')
            tree1.heading("#1", text="Account")
            tree1.heading("#2", text="Email")
            tree1.heading("#3", text="Password")
            conn = sqlite3.connect("password.db")
            cur = conn.cursor()
            cur.execute("SELECT account,email,password,rowid FROM userinfo ORDER BY rowid DESC;")
            rows = cur.fetchall()
            for row in rows:
                tree1.insert("", tk.END, values=row)
                conn.close()
            tree1.grid(row=4, column=2)

            def displaySelectedItem(a):
                # clear entries
                entry_acc.delete(0, tk.END)
                entry_email.delete(0, tk.END)
                entry_pass.delete(0, tk.END)
                entry_id.delete(0, tk.END)

                selectedItem = tree1.selection()[0]
                entry_acc.insert(0, tree1.item(selectedItem)['values'][0])
                entry_email.insert(0, tree1.item(selectedItem)['values'][1])
                entry_pass.insert(0, tree1.item(selectedItem)['values'][2])
                entry_id.insert(0, tree1.item(selectedItem)['values'][3])

            tree1.bind("<<TreeviewSelect>>", displaySelectedItem)

        btn_edit = customtkinter.CTkButton(self, text='Edit', width=5, command=edit)

        btn_destroy = customtkinter.CTkButton(self, text='Delete', width=5, command=delein)

        def displaySelectedItem(a):
            # clear entries
            entry_acc.delete(0, tk.END)
            entry_email.delete(0, tk.END)
            entry_pass.delete(0, tk.END)
            entry_id.delete(0, tk.END)

            selectedItem = tree.selection()[0]
            entry_acc.insert(0, tree.item(selectedItem)['values'][0])
            entry_email.insert(0, tree.item(selectedItem)['values'][1])
            entry_pass.insert(0, tree.item(selectedItem)['values'][2])
            entry_id.insert(0, tree.item(selectedItem)['values'][3])

        tree.bind("<<TreeviewSelect>>", displaySelectedItem)

        label_acc.grid(row=5, column=0)
        entry_acc.grid(row=6, column=0)

        label_email.grid(row=7, column=0)
        entry_email.grid(row=8, column=0)

        label_pass.grid(row=9, column=0)
        entry_pass.grid(row=10, column=0)

        btn_edit.place(x=780, y=350)
        btn_destroy.place(x=845, y=350)


if __name__ == '__main__':
    app = App()
    app.resizable(False, False)
    app.mainloop()
