# latihan praktikum
class Dosen:
    def __init__(self, nama, nidn, keahlian):
        self.nama = nama
        self.nidn = nidn
        self.keahlian = keahlian

    def profil_dosen(self):
        return f"Nama: {self.nama}, NIDN: {self.nidn}, Keahlian: {self.keahlian}"

    def ajar_mata_kuliah(self, mata_kuliah):
        print(f" {self.nama} (spesialis {self.keahlian}) sedang mengajar {mata_kuliah}...")

# object dosen
dosen1 = Dosen(" Rew ST", "123456", "Kecerdasan Buatan")
dosen2 = Dosen("Prof.Suherman", "654321", "Sistem Basis Data")

print(dosen1.profil_dosen())
dosen1.ajar_mata_kuliah("Pemrograman Python")

print(dosen2.profil_dosen())
dosen2.ajar_mata_kuliah("Manajemen Data")
