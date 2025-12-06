from tkinter import *
from tkinter import messagebox
from database import load_data, save_data


def buka_register(root):
    win = Toplevel(root)
    win.title("Register akun")
    win.geometry("400x350")
    win.configure(bg="#e3f2fd")
    

    frame = Frame(win, bg="white", padx=20, pady=20)
    frame.pack(expand=True)

    Label(frame, text="Register akun", bg="white", font=("Arial", 12, "bold")).pack(pady=10)
    
    Label(frame, text="Username", bg="white").pack()
    entry_user = Entry(frame, justify="center", bg="#f1f3f4")
    entry_user.pack()

    Label(frame, text="Password", bg="white").pack()
    entry_pass = Entry(frame, justify="center", show="*", bg="#f1f3f4")
    entry_pass.pack()

    Label(frame, text="Konfirmasi password", bg="white").pack()
    entry_confirm = Entry(frame, justify="center", show="*", bg="#f1f3f4")
    entry_confirm.pack()

    def register():
        user = entry_user.get().strip()
        pw = entry_pass.get().strip()
        pw2 = entry_confirm.get().strip()

        if not user or not pw or not pw2:
            messagebox.showerror("ERROR", "Semua kolom wajib diisi!")
            return

        data = load_data()

        for u in data["users"]:
            if u["username"] == user:
                messagebox.showerror("ERROR", "Username sudah digunakan!")
                return
            
            if pw != pw2:
                messagebox.showerror("ERROR", "pasword tidak cocok")
                return
            
            data = load_data()
            
            for u in data[user]:
                if u["username"] == user:
                    messagebox.showerror("Eror", "username sudah di gunakan")

            data["user"].append({
                "username": user,
                "password": pw
            })

        save_data(data)
        messagebox.showinfo("Sukses", "Akun berhasil dibuat!")
        win.destroy()

    Button(frame, text="Daftar", command=register, bg="#1565c0", fg="white", activebackground="#0d47a1").pack(pady=10)
