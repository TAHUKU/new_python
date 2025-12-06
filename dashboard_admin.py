from tkinter import *
from tkinter import ttk
from database import load_data


def dashboard_admin():
    win = Toplevel()
    win.title("Dashboard Admin")
    win.geometry("600x400")
    
    Label(win, text="Data Pendaftaran User", font=("Arial", 15, "bold")).pack(pady=10)
    
    tree = ttk.Treeview(win, columns=("nama", "umur", "alamat", "hp", "oleh"), show="headings")
    tree.heading("nama", text="Nama")
    tree.heading("Umur", text="umur")
    tree.heading("alamat", text="Alamat")
    tree.heading("hp", text="nomor hp")
    tree.heading("oleh", text="Didaftar oleh")
    
    
    tree.column("nama", width=120)
    tree.column("umur", width=120)
    tree.column("alamat", width=120)
    tree.column("hp", width=120)
    tree.column("oleh", width=120)
        
    tree.pack(fill=BOTH, expand=True)

    data = load_data()
    for item in data["pendaftaran"]:
        tree.insert(
            "",
            END,
            values=(
                item.get("nama", ""),
                item.get("umur", ""),
                item.get("alamat", ""),
                item.get("hp",""),
                item.get("oleh", "")
            )
        )

   