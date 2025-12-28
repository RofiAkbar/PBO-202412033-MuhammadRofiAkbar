from abc import ABC, abstractmethod
import math

# Abstraksi Bentuk
class Bentuk(ABC):
    @abstractmethod
    def luas(self):
        pass

    @abstractmethod
    def keliling(self):
        pass


class Lingkaran(Bentuk):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        return math.pi * (self.jari_jari ** 2)

    def keliling(self):
        return 2 * math.pi * self.jari_jari


class PersegiPanjang(Bentuk):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        return self.panjang * self.lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)



class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi ** 2

    def keliling(self):
        return 4 * self.sisi


# Contoh penggunaan
if __name__ == "__main__":
    l = Lingkaran(5)
    p = PersegiPanjang(4, 3)
    s1 = Persegi(6)   
    s2 = Persegi(10)  

    print(f"Luas Lingkaran: {l.luas():.2f}")
    print(f"Keliling Lingkaran: {l.keliling():.2f}")
    print(f"Luas Persegi Panjang: {p.luas()}")
    print(f"Keliling Persegi Panjang: {p.keliling()}")
    print(f"Luas Persegi (sisi 6): {s1.luas()}")
    print(f"Keliling Persegi (sisi 6): {s1.keliling()}")
    print(f"Luas Persegi (sisi 10): {s2.luas()}")
    print(f"Keliling Persegi (sisi 10): {s2.keliling()}")
