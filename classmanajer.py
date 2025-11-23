class ManajerInventori:
    def __init__(self):
        # Dictionary untuk menyimpan barang dan stoknya
        self.inventori = {}

    def tambah_barang(self, nama_barang, jumlah):
        if jumlah > 0:
            if nama_barang in self.inventori:
                self.inventori[nama_barang] += jumlah
            else:
                self.inventori[nama_barang] = jumlah
            return f"Berhasil menambah {jumlah} {nama_barang}. Stok sekarang: {self.inventori[nama_barang]}"
        return "Jumlah harus positif"

    def hapus_barang(self, nama_barang, jumlah):
        if nama_barang in self.inventori:
            if 0 < jumlah <= self.inventori[nama_barang]:
                self.inventori[nama_barang] -= jumlah
                return f"Berhasil mengurangi {jumlah} {nama_barang}. Stok sekarang: {self.inventori[nama_barang]}"
            return "Jumlah melebihi stok yang tersedia"
        return "Barang tidak ditemukan dalam inventori"

    def lihat_inventori(self):
        if not self.inventori:
            return "Inventori kosong"
        return "\n".join([f"{barang}: {stok}" for barang, stok in self.inventori.items()])


# Demonstrasi penggunaan class
if __name__ == "__main__":
    manajer = ManajerInventori()

    print(manajer.tambah_barang("Gamepad", 10))
    print(manajer.tambah_barang("Mouse", 25))
    print(manajer.hapus_barang("Gamepad", 3))
    print(manajer.hapus_barang("Mouse", 5))
    print("Inventori saat ini:")
    print(manajer.lihat_inventori())
