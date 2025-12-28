# Parent Class
class Karyawan:
    def __init__(self, nama, gaji_pokok):
        self.nama = nama
        self.gaji_pokok = gaji_pokok

    def info_gaji(self):
        return f"{self.nama} - Gaji Pokok: Rp{self.gaji_pokok}"

# Child Class: Manager
class Manager(Karyawan):
    def __init__(self, nama, gaji_pokok, tunjangan):
        super().__init__(nama, gaji_pokok)
        self.tunjangan = tunjangan

    def info_gaji(self):
        total = self.gaji_pokok + self.tunjangan
        return f"{self.nama} (Manager) - Gaji Total: Rp{total}"

# Child Class: Programmer
class Programmer(Karyawan):
    def __init__(self, nama, gaji_pokok, bonus):
        super().__init__(nama, gaji_pokok)
        self.bonus = bonus

    def info_gaji(self):
        total = self.gaji_pokok + self.bonus
        return f"{self.nama} (Programmer) - Gaji Total: Rp{total}"

# Composition: Departemen
class Departemen:
    def __init__(self, nama_departemen):
        self.nama_departemen = nama_departemen
        self.daftar_karyawan = []

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)

    def tampilkan_karyawan(self):
        print(f"Daftar Karyawan di Departemen {self.nama_departemen}:")
        for karyawan in self.daftar_karyawan:
            print(karyawan.info_gaji())

# Instansiasi dan Eksekusi
if __name__ == "__main__":
    # Buat objek Manager
    manager1 = Manager("Andi", 7000000, 3000000)
    manager2 = Manager("Budi", 7500000, 2500000)

    # Buat objek Programmer
    programmer1 = Programmer("Citra", 6000000, 1500000)
    programmer2 = Programmer("Dewi", 6200000, 1800000)

    # Buat Departemen dan tambahkan karyawan
    departemen_IT = Departemen("IT")
    departemen_IT.tambah_karyawan(manager1)
    departemen_IT.tambah_karyawan(manager2)
    departemen_IT.tambah_karyawan(programmer1)
    departemen_IT.tambah_karyawan(programmer2)

    # Tampilkan info gaji semua karyawan
    departemen_IT.tampilkan_karyawan()
