class Mahasiswa:
    # Class attribute
    universitas = "STITEK Bontang"

    # Constructor (__init__)
    def __init__(self, nama, nim, jurusan, ipk=0.0):
        # 2a. Instance attributes
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    # perkenalan_diri
    def perkenalan_diri(self):
        print(f"Halo, saya {self.nama} ({self.nim}) dari jurusan {self.jurusan}.")
        print(f"Saya kuliah di {Mahasiswa.universitas}.")

    # Method update_ipk
    def update_ipk(self, ipk_baru):
        self.ipk = ipk_baru
        print(f"IPK {self.nama} telah diperbarui menjadi {self.ipk:.2f}")

    # predikat_kelulusan
    def predikat_kelulusan(self):
        if self.ipk >= 3.5:
            predikat = "Cum Laude"
        elif self.ipk >= 3.0:
            predikat = "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            predikat = "Memuaskan"
        elif self.ipk >= 2.0:
            predikat = "Lulus"
        else:
            predikat = "Belum Lulus"
        print(f"Predikat kelulusan {self.nama}: {predikat}")
# mahasiswa
mhs1 = Mahasiswa("Rofi", "202412001", "Informatika", 1.6)
mhs2 = Mahasiswa("Cakra", "202412002", "Informatika", 2.9)
mhs3 = Mahasiswa("Abror", "202412003", "Informatika")

# Demonstrasikan semua method
print("=== Perkenalan Diri ===")
mhs1.perkenalan_diri()
mhs2.perkenalan_diri()
mhs3.perkenalan_diri()

print("\n=== Update IPK ===")
mhs3.update_ipk(2.4)

print("\n=== Predikat Kelulusan ===")
mhs1.predikat_kelulusan()
mhs2.predikat_kelulusan()
mhs3.predikat_kelulusan()
