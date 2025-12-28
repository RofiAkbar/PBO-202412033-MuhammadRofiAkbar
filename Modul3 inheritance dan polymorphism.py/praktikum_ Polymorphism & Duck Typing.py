class Laptop:
    def nyalakan(self):
        return "Laptop dinyalakan, siap digunakan."
    

class Smartphone:
    def nyalakan(self):
        return "Smartphone dinyalakan, siap digunakan."

def tes_nyala(obj):
    print(obj.nyalakan())

# Instansiasi objek
l = Laptop()
s = Smartphone()

# Duck typing dalam aksi
tes_nyala(l)
tes_nyala(s)
