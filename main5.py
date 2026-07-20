nama = input("Masukkan nama Anda: ")
barang = input("Masukkan nama barang yang dibeli: ")
harga = int(input("Masukkan harga barang: "))
jumlah = int(input("Masukkan jumlah barang yang dibeli: "))

nama_bersih = nama.strip().title()

total_awal = harga * jumlah

if total_awal >= 500000:
    diskon = total_awal * 0.1
else:
    diskon = 0
    
total_akhir = total_awal - diskon

print("=== STRUK PEMBELIAN ===")
print(f"Nama Pembeli: {nama_bersih}")
print(f"Barang: {barang}")
print(f"Harga Satuan: Rp{harga:,}")
print(f"Jumlah Barang: {jumlah}")
print(f"Total Awal: Rp{total_awal:,}")
if diskon > 0:
    print(f"Diskon: Rp{diskon:,}")
print(f"Total Akhir: Rp{total_akhir:,}")