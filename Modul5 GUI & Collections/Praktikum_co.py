# modul4_buku.py


class Buku:
    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

    def info(self):
        return f"{self.judul} — {self.penulis} ({self.tahun})"



daftar_buku = [
    Buku("Laskar Pelangi", "Andrea Hirata", 2005),
    Buku("Bumi Manusia", "Pramoedya Ananta Toer", 1980),
    Buku("Negeri 5 Menara", "A. Fuadi", 2009),
    Buku("Ayat-Ayat Cinta", "Habiburrahman El Shirazy", 2004),
    Buku("Ranah 3 Warna", "A. Fuadi", 2011),
]



def cari_buku_by_penulis(nama_penulis, koleksi):
    kunci = nama_penulis.strip().casefold()
    return [b for b in koleksi if b.penulis.casefold() == kunci]


if __name__ == "__main__":
    print("=== Pencarian Buku Berdasarkan Penulis ===")
    penulis = input("Masukkan nama penulis: ").strip()

    hasil = cari_buku_by_penulis(penulis, daftar_buku)

    if not hasil:
        print(f"Tidak ada buku dari penulis: {penulis}")
    else:
        print(f"Ditemukan {len(hasil)} buku dari penulis: {penulis}")
        for i, b in enumerate(hasil, start=1):
            print(f"{i}. {b.info()}")
