class Dosen:
    def __init__(self, nama, nidn):
        self.nama = nama
        self.nidn = nidn

    def ajar_mata_kuliah(self, mata_kuliah):
        return f"Nama saya {self.nama} (NIDN: {self.nidn}), saya mengajar mata kuliah {mata_kuliah}"

# Instansiasi objek
dosen1 = Dosen("Dr. Suherman", "123456")
dosen2 = Dosen("Prof. Nanang", "654321")

# Pemanggilan method
print(dosen1.ajar_mata_kuliah("Pemrograman Python"))
print(dosen2.ajar_mata_kuliah("Struktur Data"))

