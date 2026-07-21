print("=== KALKULATOR BIAYA SKS MAHASISWA ===")

try:
    total_biaya = int(input("Masukkan Total Biaya Kuliah (Rp): "))
    jumlah_sks = int(input("Masukkan Jumlah SKS yang Diambil: "))
    
    biaya_per_sks = total_biaya / jumlah_sks
    
    print(f"Biaya rata-rata per 1 SKS adalah: Rp{biaya_per_sks:,.2f}")


except ValueError:
    print("Input tidak valid. Silakan masukkan angka untuk total biaya dan jumlah SKS.")
    pass

except ZeroDivisionError:
    if jumlah_sks == 0:
        print("Jumlah SKS tidak boleh 0. Silakan masukkan jumlah SKS yang valid.")
    pass

finally:
    print("=== Sesi Perhitungan Selesai ===")