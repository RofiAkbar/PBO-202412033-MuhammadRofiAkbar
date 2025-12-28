from abc import ABC, abstractmethod

# ✅ 1. Abstraction Class
class Pengguna(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def akses(self):
        pass


class PoinTidakValidError(Exception):
    """Custom exception jika poin tidak valid (<0)."""
    pass


# ✅ 1. Class turunan Member
class Member(Pengguna):
    def __init__(self, nama, poin):
        super().__init__(nama)
        if poin < 0:
            raise PoinTidakValidError("Poin tidak boleh negatif!")
        self.poin = poin

    def akses(self):
        return f"{self.nama} memiliki hak akses sebagai Member."

    # ✅ 2. Special Methods
    def __str__(self):
        return f"Member: {self.nama} – Poin: {self.poin}"

    def __add__(self, other):
        if isinstance(other, Member):
            return self.poin + other.poin
        return NotImplemented

    def __len__(self):
        return len(self.nama)


if __name__ == "__main__":
    try:
        # ✅ 3. Exception Handling: input poin dari user
        nama1 = input("Masukkan nama member pertama: ").strip()
        p1 = input("Masukkan poin member pertama: ").strip()

        if p1 == "":
            raise ValueError("Input poin tidak boleh kosong!")
        p1 = int(p1)

        nama2 = input("Masukkan nama member kedua: ").strip()
        p2 = input("Masukkan poin member kedua: ").strip()

        if p2 == "":
            raise ValueError("Input poin tidak boleh kosong!")
        p2 = int(p2)

        # ✅ 4. Custom Exception: jika poin < 0
        m1 = Member(nama1, p1)
        m2 = Member(nama2, p2)

        # ✅ 5. Buat 2 objek Member dan tampilkan
        print("\n=== Info Member ===")
        print(m1)  # __str__
        print(m2)
        print("Hak akses:", m1.akses())
        print("Jumlah poin:", m1 + m2)  # __add__
        print("Panjang nama member pertama:", len(m1))  # __len__

    except ValueError as ve:
        print("Input salah:", ve)

    except PoinTidakValidError as e:
        print("Error:", e)

    finally:
        print("Selesai memproses input.")
