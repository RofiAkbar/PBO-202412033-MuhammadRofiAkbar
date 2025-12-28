# Modul4 > validasi_umur.py

class UmurTidakValidError(Exception):
    """Kesalahan untuk umur yang tidak masuk akal."""
    pass

class UmurTerlaluMudaError(Exception):
    """Kesalahan jika umur terlalu muda (<5)."""
    pass

class UmurTerlaluTuaError(Exception):
    """Kesalahan jika umur terlalu tua (>100)."""
    pass

class AkunTidakDiizinkanError(Exception):
    """Kesalahan jika umur belum cukup untuk daftar akun."""
    pass

def set_umur(umur):
    if umur < 0:
        raise UmurTidakValidError("Umur tidak boleh negatif!")
    if umur < 5:
        raise UmurTerlaluMudaError("Umur terlalu muda untuk diproses (<5).")
    if umur > 100:
        raise UmurTerlaluTuaError("Umur terlalu tua (>100).")
    return umur

def daftar_akun(umur):
    if umur < 18:
        raise AkunTidakDiizinkanError("Umur belum cukup untuk mendaftar akun (minimal 18 tahun).")
    print("Akun berhasil didaftarkan!")

if __name__ == "__main__":
    while True:
        try:
            u = input("Masukkan umur: ").strip()

            if u == "":
                raise ValueError("Input tidak boleh kosong!")

            umur = int(u)
            umur = set_umur(umur)
            print("Umur valid:", umur)

            daftar_akun(umur)
            break  # keluar dari loop jika semua valid

        except ValueError as ve:
            print("Input salah:", ve)

        except UmurTidakValidError as e:
            print(e)

        except UmurTerlaluMudaError as e:
            print(e)

        except UmurTerlaluTuaError as e:
            print(e)

        except AkunTidakDiizinkanError as e:
            print(e)

        finally:
            print("Selesai memproses input.\n")
