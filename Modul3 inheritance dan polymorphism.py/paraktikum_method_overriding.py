class Bentuk:
    def luas(self):
        return 0
class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi * self.sisi


class Lingkaran(Bentuk):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        return 3.14 * self.jari_jari * self.jari_jari
# Instansiasi objek
bentuk = Bentuk()
persegi = Persegi(5)        
lingkaran = Lingkaran(7)    

# Pemanggilan method luas()
print("Luas Bentuk:", bentuk.luas())
print("Luas Persegi:", persegi.luas())
print("Luas Lingkaran:", lingkaran.luas())
