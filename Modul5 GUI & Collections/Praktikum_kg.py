import tkinter as tk
from tkinter import messagebox

# b. Gunakan class untuk mengorganisir komponen GUI
class KonversiSuhuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Konversi Suhu")
        self.root.geometry("300x200")

        # a. Komponen GUI: Label, Entry, Button
        self.label = tk.Label(root, text="Masukkan suhu (°C):", font=("Arial", 12))
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, width=20)
        self.entry.pack(pady=5)

        self.button_konversi = tk.Button(root, text="Konversi", command=self.konversi)
        self.button_konversi.pack(pady=5)

        self.button_keluar = tk.Button(root, text="Keluar", command=root.quit)
        self.button_keluar.pack(pady=5)

    # c. Validasi input dan konversi suhu
    def konversi(self):
        nilai = self.entry.get().strip()
        if not nilai:
            messagebox.showwarning("Peringatan", "Input tidak boleh kosong!")
            return
        try:
            celsius = float(nilai)
            fahrenheit = (celsius * 9/5) + 32
            messagebox.showinfo("Hasil Konversi", f"{celsius:.2f} °C = {fahrenheit:.2f} °F")
        except ValueError:
            messagebox.showerror("Error", "Input harus berupa angka!")


if __name__ == "__main__":
    root = tk.Tk()
    app = KonversiSuhuApp(root)
    root.mainloop()
