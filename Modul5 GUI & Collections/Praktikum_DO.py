
class Pelanggan:
    def __init__(self, id_pelanggan, nama, email):
        self.id_pelanggan = id_pelanggan
        self.nama = nama
        self.email = email

    def info(self):
        return f"{self.id_pelanggan} - {self.nama} ({self.email})"



pelanggan_db = {
    "C001": Pelanggan("C001", "Ali", "ali@example.com"),
    "C002": Pelanggan("C002", "Budi", "budi@example.com"),
    "C003": Pelanggan("C003", "Citra", "citra@example.com"),
}


def tambah_pelanggan(db, pelanggan):
    if pelanggan.id_pelanggan in db:
        raise ValueError(f"ID {pelanggan.id_pelanggan} sudah ada.")
    if "@" not in pelanggan.email:
        raise ValueError("Email tidak valid.")
    db[pelanggan.id_pelanggan] = pelanggan
    print(f"Pelanggan ditambahkan: {pelanggan.info()}")


def hapus_pelanggan(db, id_pelanggan):
    if id_pelanggan in db:
        removed = db.pop(id_pelanggan)
        print(f"Pelanggan dihapus: {removed.info()}")
    else:
        print(f"ID {id_pelanggan} tidak ditemukan.")


def cari_pelanggan(db, id_pelanggan):
    return db.get(id_pelanggan, None)


# d. Tampilkans eluruh daftar pelanggan.
def tampilkan_semua(db):
    print("=== Daftar Pelanggan ===")
    if not db:
        print("(kosong)")
        return
    for pid, p in db.items():
        print(p.info())


if __name__ == "__main__":
    # Demo eksekusi untuk laporan praktikum (non-interaktif, langsung jalan)
    tampilkan_semua(pelanggan_db)

    print("\n=== Cari Pelanggan ===")
    target = "C002"
    hasil = cari_pelanggan(pelanggan_db, target)
    if hasil:
        print(f"Ditemukan: {hasil.info()}")
    else:
        print(f"ID {target} tidak ditemukan.")

    print("\n=== Tambah Pelanggan ===")
    try:
        tambah_pelanggan(pelanggan_db, Pelanggan("C004", "Dewi", "dewi@example.com"))
        
        tambah_pelanggan(pelanggan_db, Pelanggan("C004", "Dewi 2", "dewi2@example.com"))
    except ValueError as ve:
        print("Input salah:", ve)

    print("\n=== Hapus Pelanggan ===")
    hapus_pelanggan(pelanggan_db, "C001")  
    hapus_pelanggan(pelanggan_db, "C999")  

    print("\n=== Daftar Akhir ===")
    tampilkan_semua(pelanggan_db)
