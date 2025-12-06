from tkinter import *
from tkinter import messagebox
from database import load_data
from dashboard_user import dashboard_user
from dashboard_admin import dashboard_admin
from register import buka_register


def halaman_login(root):
    root.title("Login")
    root.geometry("400x400")
    root.configure(bg="#e3f2fd")
    
    frame = Frame(root, bg="white", padx=20, pady=20, highlightthickness=2, highlightbackground="#bbdefb")
    frame.pack(expand=True)
    Label(frame, text="Login", font=("Arial", 16, "bold"), bg="white", fg="#1565c0").pack(pady=10)
    
    
    Label(frame, text="Username", bg="white").pack()
    entry_user = Entry(frame, justify="center", bg="#f1f3f4")
    entry_user.pack(pady=5)
    
    Label(frame, text="Password", bg="white").pack()
    entry_pswd = Entry(frame, justify="center", show="?", bg="#f1f3f4")
    entry_pswd.pack(pady=5)
    
    def login():
        user = entry_user.get().strip()
        pswd = entry_pswd.get().strip()

        if not user or not pswd:
            messagebox.showerror("Error", "Isi semua kolom!")
            return
        
        data = load_data()
        admin = data["admin"]
        users = data["users"]

        # Login admin
        if user == admin["username"] and pswd == admin["password"]:
            messagebox.showinfo("Berhasil", "Login sebagai Admin")
            root.withdraw()
            
            dashboard_admin()
            return

        # Login user
        for u in users:
            if u["username"] == user and u["password"] == pswd:
                messagebox.showinfo("Berhasil", f"Selamat datang {user}")
                
                root.withdraw()
                
                dashboard_user(user)
                return

        messagebox.showerror("Gagal", "Username atau password salah!")

    Button(frame, text="Login", command=login , bg="#1565c0", fg="white", activebackground="#0d47a1").pack(pady=10)
    Button(frame, text="Register", command=lambda: buka_register(root), bg="#90caf9", fg="black", activebackground="#64b5f6").pack()
