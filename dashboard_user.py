from tkinter import *
from tkinter import messagebox
from database import load_data, save_data


def dashboard_user(username):
    win = Toplevel()
    win.title("Dashboard User")
    win.geometry("400x300")
    

    Label(win, text=f"Selamat datang, {username}", font=("Arial", 14)).pack(pady=10)
    Label(win, text="Form Pendaftaran").pack()

    Label(win, text="Nama").pack()
    entry_nama = Entry(win)
    entry_nama.pack()
    
    Label(win, text="Umur").pack()
    entry_umur = Entry(win)
    entry_umur.pack()
    
    Label(win, text="Alamat").pack()
    entry_alamat = Entry(win)
    entry_alamat.pack()
    
    Label(win, text="nomor Hp").pack()
    entry_hp = Entry(win)
    entry_hp.pack()

    def simpan():
        nama = entry_nama.get().strip()
        alamat = entry_alamat.get().strip()
        umur = entry_umur.get().strip()
        hp = entry_hp.get().strip()

        if not nama or not alamat:
            messagebox.showerror("Error", "Nama & alamat wajib diisi!")
            return

        data = load_data()
        data["pendaftaran"].append({
            "nama": nama,
            "Umur": umur,
            "alamat": alamat,
            "nomer hp": hp,
            "oleh": username
        })
        save_data(data)

        messagebox.showinfo("Berhasil", "Data pendaftaran tersimpan!")
        entry_nama.delete(0, END)
        entry_alamat.delete(0, END)
      
        

    Button(win, text="Simpan", command=simpan).pack(pady=10)
