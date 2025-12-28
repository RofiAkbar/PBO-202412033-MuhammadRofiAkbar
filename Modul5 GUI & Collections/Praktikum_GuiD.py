import tkinter as tk
from tkinter import messagebox


class AplikasiGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Latihan Praktikum GUI")
        self.root.geometry("300x200")

        # Label
        self.label = tk.Label(root, text="Masukkan teks:", font=("Arial", 12))
        self.label.pack(pady=10)

        # Entry
        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=10)

        # Button untuk menampilkan isi Entry
        self.button_tampil = tk.Button(root, text="Tampilkan", command=self.tampilkan_isi)
        self.button_tampil.pack(pady=5)

        # c. Button untuk menghapus isi Entry
        self.button_hapus = tk.Button(root, text="Hapus", command=self.hapus_isi)
        self.button_hapus.pack(pady=5)

    # b. Fungsi untuk menampilkan isi Entry di messagebox
    def tampilkan_isi(self):
        teks = self.entry.get()
        if teks.strip():
            messagebox.showinfo("Isi Entry", f"Anda mengetik: {teks}")
        else:
            messagebox.showwarning("Peringatan", "Entry masih kosong!")

    # c. Fungsi untuk menghapus isi Entry
    def hapus_isi(self):
        self.entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiGUI(root)
    root.mainloop()
