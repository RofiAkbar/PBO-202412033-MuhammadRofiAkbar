import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class Tugas:
    def __init__(self, judul, status="Belum Selesai"):
        self.judul = judul
        self.status = status

    def selesai(self):
        self.status = "Selesai"

    def to_tuple(self):
        return (self.judul, self.status)


class AplikasiToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("Manajemen Tugas (To-Do List)")
        self.root.geometry("500x400")

        # List of objects
        self.daftar_tugas = []

        # Frame input
        frame_input = tk.Frame(root, padx=10, pady=10)
        frame_input.pack()

        tk.Label(frame_input, text="Judul Tugas:").grid(row=0, column=0, sticky=tk.W)
        self.entry_judul = tk.Entry(frame_input, width=30)
        self.entry_judul.grid(row=0, column=1, padx=5, pady=5)

        # Frame tombol
        frame_tombol = tk.Frame(root, padx=10, pady=10)
        frame_tombol.pack()

        tk.Button(frame_tombol, text="Tambah", command=self.tambah_tugas).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Hapus", command=self.hapus_tugas).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Edit", command=self.edit_tugas).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Tandai Selesai", command=self.selesai_tugas).pack(side=tk.LEFT, padx=5)

      
        frame_tabel = tk.Frame(root, padx=10, pady=10)
        frame_tabel.pack(fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(frame_tabel, columns=("Judul", "Status"), show="headings")
        self.tree.heading("Judul", text="Judul")
        self.tree.heading("Status", text="Status")
        self.tree.pack(fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(frame_tabel, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    #Fitur tambah
    def tambah_tugas(self):
        judul = self.entry_judul.get().strip()
        if judul:
            tugas_baru = Tugas(judul)
            self.daftar_tugas.append(tugas_baru)
            self.tree.insert("", tk.END, values=tugas_baru.to_tuple())
            self.entry_judul.delete(0, tk.END)
        else:
            messagebox.showwarning("Peringatan", "Judul tugas tidak boleh kosong!")

    #Fitur hapus
    def hapus_tugas(self):
        selected_item = self.tree.selection()
        if selected_item:
            index = self.tree.index(selected_item[0])
            self.tree.delete(selected_item[0])
            del self.daftar_tugas[index]
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas yang akan dihapus!")

    #Fitur edit
    def edit_tugas(self):
        selected_item = self.tree.selection()
        if selected_item:
            index = self.tree.index(selected_item[0])
            tugas = self.daftar_tugas[index]
            judul_baru = simpledialog.askstring("Edit Tugas", "Masukkan judul baru:", initialvalue=tugas.judul)
            if judul_baru:
                tugas.judul = judul_baru
                self.tree.item(selected_item[0], values=tugas.to_tuple())
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas yang akan diedit!")

    #Fitur tandai selesai
    def selesai_tugas(self):
        selected_item = self.tree.selection()
        if selected_item:
            index = self.tree.index(selected_item[0])
            tugas = self.daftar_tugas[index]
            tugas.selesai()
            self.tree.item(selected_item[0], values=tugas.to_tuple())
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas yang akan ditandai selesai!")


if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiToDoList(root)
    root.mainloop()
