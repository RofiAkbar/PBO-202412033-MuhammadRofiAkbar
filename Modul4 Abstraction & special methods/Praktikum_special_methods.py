class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

    def __str__(self):
        return f"Nama: {self.nama}, Nilai: {self.nilai}"

    def __gt__(self, other):
        return self.nilai > other.nilai

    def __add__(self, other):
        return self.nilai + other.nilai

    def __mul__(self, faktor):
        return self.nilai * faktor

    # ✅ b. Method __len__ → panjang nama mahasiswa
    def __len__(self):
        return len(self.nama)

    # ✅ c. Method __eq__ → sama jika nilai sama
    def __eq__(self, other):
        return self.nilai == other.nilai


# ✅ d. Contoh penggunaan
if __name__ == "__main__":
    m1 = Mahasiswa("Pouster", 80)
    m2 = Mahasiswa("Ahmad", 90)
    m3 = Mahasiswa("Budi", 80)

    # Representasi string
    print(m1)
    print(m2)
    print(m3)

    # Panjang nama (len)
    print(f"Panjang nama {m1.nama}: {len(m1)}")
    print(f"Panjang nama {m2.nama}: {len(m2)}")

    # Perbandingan kesetaraan nilai
    print("Apakah m1 dan m3 nilainya sama?", m1 == m3)
    print("Apakah m1 dan m2 nilainya sama?", m1 == m2)

    # Operasi matematika
    print("Total nilai m1 + m2 =", m1 + m2)
    print("Nilai m2 x 2 =", m2 * 2)

    # Sorted berdasarkan nilai
    list_mahasiswa = [m1, m2, m3]
    sorted_list = sorted(list_mahasiswa, key=lambda x: x.nilai)
    print("Urutan mahasiswa berdasarkan nilai:")
    for m in sorted_list:
        print(m)
