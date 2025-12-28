class Penulis:
    def __init__(self, nama):
        self.nama = nama

class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis  

    def info(self):
        return f"Buku '{self.judul}' ditulis oleh {self.penulis.nama}"

# Instansiasi objek
penulis1 = Penulis("Tere Liye")
buku1 = Buku("Hafalan Shalat Delisa", penulis1)

# Akses data penulis dari objek buku
print(buku1.info())
print("Nama Penulis:", buku1.penulis.nama)



