import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from typing import Dict, List, Optional

class Mahasiswa:
    def __init__(self, nim: str, nama: str, jurusan: str, ipk: float):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan
        self.ipk = ipk

    def info(self) -> str:
        return f"{self.nim} - {self.nama} | {self.jurusan} | IPK: {self.ipk:.2f}"

    def update_ipk(self, ipk_baru: float):
        self.ipk = ipk_baru



class MahasiswaDB:
    def __init__(self):
        self.data: Dict[str, Mahasiswa] = {}

    def tambah(self, mhs: Mahasiswa):
        if mhs.nim in self.data:
            raise ValueError(f"NIM {mhs.nim} sudah terdaftar.")
        self.data[mhs.nim] = mhs

    def hapus(self, nim: str) -> bool:
        return self.data.pop(nim, None) is not None

    def cari_by_nim(self, nim: str) -> Optional[Mahasiswa]:
        return self.data.get(nim)

    def cari_by_nama(self, query: str) -> List[Mahasiswa]:
        q = query.strip().lower()
        return [m for m in self.data.values() if q in m.nama.lower()]

    def semua(self) -> List[Mahasiswa]:
        return list(self.data.values())

    def filter_jurusan(self, jurusan: str) -> List[Mahasiswa]:
        j = jurusan.strip().lower()
        return [m for m in self.data.values() if m.jurusan.lower() == j]

    def rata_rata_ipk(self) -> float:
        vals = [m.ipk for m in self.data.values()]
        return sum(vals) / len(vals) if vals else 0.0

    def ipk_tertinggi(self) -> Optional[Mahasiswa]:
        return max(self.data.values(), key=lambda m: m.ipk, default=None)


class AppMahasiswa:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Manajemen Mahasiswa")
        self.root.geometry("820x540")

        self.db = MahasiswaDB()

        # a. Frame input data
        frame_input = tk.LabelFrame(root, text="Input Data Mahasiswa", padx=10, pady=10)
        frame_input.pack(fill=tk.X, padx=10, pady=8)

        tk.Label(frame_input, text="NIM").grid(row=0, column=0, sticky="w")
        self.entry_nim = tk.Entry(frame_input, width=20)
        self.entry_nim.grid(row=0, column=1, padx=6, pady=4)

        tk.Label(frame_input, text="Nama").grid(row=0, column=2, sticky="w")
        self.entry_nama = tk.Entry(frame_input, width=24)
        self.entry_nama.grid(row=0, column=3, padx=6, pady=4)

        tk.Label(frame_input, text="Jurusan").grid(row=1, column=0, sticky="w")
        self.entry_jurusan = tk.Entry(frame_input, width=20)
        self.entry_jurusan.grid(row=1, column=1, padx=6, pady=4)

        tk.Label(frame_input, text="IPK").grid(row=1, column=2, sticky="w")
        self.entry_ipk = tk.Entry(frame_input, width=24)
        self.entry_ipk.grid(row=1, column=3, padx=6, pady=4)

        # b. Tombol CRUD
        frame_crud = tk.Frame(root)
        frame_crud.pack(fill=tk.X, padx=10)

        tk.Button(frame_crud, text="Tambah", command=self.action_tambah).pack(side=tk.LEFT, padx=5, pady=6)
        tk.Button(frame_crud, text="Update IPK", command=self.action_update_ipk).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_crud, text="Hapus", command=self.action_hapus).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_crud, text="Reset Form", command=self.reset_form).pack(side=tk.LEFT, padx=5)

        # d. Pencarian dan e. Filter jurusan
        frame_filter = tk.LabelFrame(root, text="Pencarian & Filter", padx=10, pady=10)
        frame_filter.pack(fill=tk.X, padx=10, pady=8)

        tk.Label(frame_filter, text="Cari NIM / Nama:").pack(side=tk.LEFT)
        self.entry_cari = tk.Entry(frame_filter, width=24)
        self.entry_cari.pack(side=tk.LEFT, padx=5)
        tk.Button(frame_filter, text="Cari", command=self.action_cari).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_filter, text="Tampilkan Semua", command=self.render_semua).pack(side=tk.LEFT, padx=5)

        tk.Label(frame_filter, text="Filter Jurusan:").pack(side=tk.LEFT, padx=20)
        self.entry_filter_jurusan = tk.Entry(frame_filter, width=18)
        self.entry_filter_jurusan.pack(side=tk.LEFT, padx=5)
        tk.Button(frame_filter, text="Filter", command=self.action_filter).pack(side=tk.LEFT, padx=5)

        # c. Treeview daftar mahasiswa
        frame_table = tk.LabelFrame(root, text="Daftar Mahasiswa", padx=10, pady=10)
        frame_table.pack(fill=tk.BOTH, expand=True, padx=10, pady=8)

        self.tree = ttk.Treeview(frame_table, columns=("nim", "nama", "jurusan", "ipk"), show="headings")
        self.tree.heading("nim", text="NIM")
        self.tree.heading("nama", text="Nama")
        self.tree.heading("jurusan", text="Jurusan")
        self.tree.heading("ipk", text="IPK")
        self.tree.column("nim", width=120)
        self.tree.column("nama", width=220)
        self.tree.column("jurusan", width=160)
        self.tree.column("ipk", width=80, anchor="center")
        self.tree.pack(fill=tk.BOTH, expand=True)

        scroll = ttk.Scrollbar(frame_table, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)

        
        frame_extra = tk.LabelFrame(root, text="Fitur Tambahan", padx=10, pady=10)
        frame_extra.pack(fill=tk.X, padx=10, pady=8)

        tk.Button(frame_extra, text="Rata-rata IPK", command=self.action_rata_ipk).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_extra, text="IPK Tertinggi", command=self.action_ipk_tertinggi).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_extra, text="Export ke TXT", command=self.action_export).pack(side=tk.LEFT, padx=5)

        # seed data opsional untuk demo
        self.seed_demo()
        self.render_semua()

    # Validasi input
    def validate_inputs(self, nim: str, nama: str, jurusan: str, ipk_str: str) -> Optional[float]:
        if not nim.strip() or not nama.strip() or not jurusan.strip() or not ipk_str.strip():
            messagebox.showwarning("Peringatan", "Semua field wajib diisi.")
            return None
        try:
            ipk = float(ipk_str)
        except ValueError:
            messagebox.showerror("Error", "IPK harus berupa angka.")
            return None
        if not (0.0 <= ipk <= 4.0):
            messagebox.showerror("Error", "IPK harus di antara 0.00 dan 4.00.")
            return None
        return ipk

    # CRUD actions
    def action_tambah(self):
        nim = self.entry_nim.get()
        nama = self.entry_nama.get()
        jurusan = self.entry_jurusan.get()
        ipk_str = self.entry_ipk.get()

        ipk = self.validate_inputs(nim, nama, jurusan, ipk_str)
        if ipk is None:
            return
        try:
            self.db.tambah(Mahasiswa(nim, nama, jurusan, ipk))
            messagebox.showinfo("Sukses", "Mahasiswa berhasil ditambahkan.")
            self.render_semua()
            self.reset_form()
        except ValueError as e:
            messagebox.showerror("Gagal", str(e))

    def action_update_ipk(self):
        nim = self.entry_nim.get().strip()
        ipk_str = self.entry_ipk.get().strip()
        if not nim:
            messagebox.showwarning("Peringatan", "Masukkan NIM untuk update IPK.")
            return
        ipk = self.validate_inputs(nim, "x", "x", ipk_str)  # hanya validasi IPK
        if ipk is None:
            return
        mhs = self.db.cari_by_nim(nim)
        if not mhs:
            messagebox.showinfo("Info", f"Mahasiswa dengan NIM {nim} tidak ditemukan.")
            return
        mhs.update_ipk(ipk)
        messagebox.showinfo("Sukses", f"IPK NIM {nim} diupdate ke {ipk:.2f}.")
        self.render_semua()

    def action_hapus(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Peringatan", "Pilih baris yang akan dihapus.")
            return
        nim = self.tree.item(selected[0])["values"][0]
        if self.db.hapus(nim):
            messagebox.showinfo("Sukses", f"Mahasiswa NIM {nim} dihapus.")
            self.render_semua()

    def action_cari(self):
        query = self.entry_cari.get().strip()
        if not query:
            messagebox.showwarning("Peringatan", "Masukkan kata kunci NIM atau Nama.")
            return
        if query.isdigit():
            hasil = []
            m = self.db.cari_by_nim(query)
            if m:
                hasil = [m]
        else:
            hasil = self.db.cari_by_nama(query)
        self.render_list(hasil)

    def action_filter(self):
        jurusan = self.entry_filter_jurusan.get().strip()
        if not jurusan:
            messagebox.showwarning("Peringatan", "Masukkan jurusan untuk filter.")
            return
        hasil = self.db.filter_jurusan(jurusan)
        self.render_list(hasil)

    # Rendering
    def render_semua(self):
        self.render_list(self.db.semua())

    def render_list(self, items: List[Mahasiswa]):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for m in items:
            self.tree.insert("", tk.END, values=(m.nim, m.nama, m.jurusan, f"{m.ipk:.2f}"))

    def reset_form(self):
        self.entry_nim.delete(0, tk.END)
        self.entry_nama.delete(0, tk.END)
        self.entry_jurusan.delete(0, tk.END)
        self.entry_ipk.delete(0, tk.END)
        self.entry_cari.delete(0, tk.END)
        self.entry_filter_jurusan.delete(0, tk.END)

   
    def action_rata_ipk(self):
        rata = self.db.rata_rata_ipk()
        messagebox.showinfo("Rata-rata IPK", f"Rata-rata IPK: {rata:.2f}")

    def action_ipk_tertinggi(self):
        m = self.db.ipk_tertinggi()
        if m:
            messagebox.showinfo("IPK Tertinggi", f"{m.info()}")
        else:
            messagebox.showinfo("IPK Tertinggi", "Belum ada data.")

    def action_export(self):
        try:
            with open("data_mahasiswa.txt", "w", encoding="utf-8") as f:
                for m in self.db.semua():
                    f.write(f"{m.nim},{m.nama},{m.jurusan},{m.ipk:.2f}\n")
            messagebox.showinfo("Export", "Data diexport ke data_mahasiswa.txt")
        except Exception as e:
            messagebox.showerror("Export Gagal", str(e))

    # seed demo data
    def seed_demo(self):
        demo = [
            Mahasiswa("22001", "Rofi", "Informatika", 3.45),
            Mahasiswa("22002", "Bouya", "Sistem Informasi", 3.10),
            Mahasiswa("22003", "Yumi", "Informatika", 3.85),
        ]
        for m in demo:
            self.db.data[m.nim] = m


if __name__ == "__main__":
    root = tk.Tk()
    app = AppMahasiswa(root)
    root.mainloop()
