class Kendaraan:
    # Class attribute
    bahan_bakar = "Bensin"

    # Constructor
    def __init__(self, merk, warna, tahun):
        # Instance attributes
        self.merk = merk
        self.warna = warna
        self.tahun = tahun

    def info_kendaraan(self):
        return f"{self.merk} berwarna {self.warna} keluaran tahun {self.tahun}"


# Instansiasi object
mobil1 = Kendaraan("Toyota", "Hitam", 2020)
motor1 = Kendaraan("Honda", "Merah", 2018)

# Output instance attribute
print("=== Instance Attribute ===")
print(mobil1.info_kendaraan())
print(motor1.info_kendaraan())

# Output class attribute
print("\n=== Class Attribute ===")
print(f"Mobil1 Bahan Bakar: {mobil1.bahan_bakar}")
print(f"Motor1 Bahan Bakar: {motor1.bahan_bakar}")
print(f"Class Kendaraan Bahan Bakar: {Kendaraan.bahan_bakar}")
