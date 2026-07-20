stok_gudang = [
    {"id_barang": "BRG01", "nama_barang": "Laptop Kantor", "stok": 12},
    {"id_barang": "BRG02", "nama_barang": "Mouse Wireless", "stok": 3},
    {"id_barang": "BRG03", "nama_barang": "Keyboard Mekanik", "stok": 25},
    {"id_barang": "BRG04", "nama_barang": "Monitor 24 Inch", "stok": 4},
    {"id_barang": "BRG05", "nama_barang": "Kabel HDMI 2M", "stok": 50}
]

def cek_status_stok(stok):
    if stok < 5:
        return "Stok Menipis"
    else:
        return "Stok Aman"
    
jumlah_barang_kritis = 0

print("=== LAPORAN MANAJEMEN STOK GUDANG ===")

for barang in stok_gudang:
    id_barang = barang["id_barang"]
    nama_barang = barang["nama_barang"]
    stok = barang["stok"]
    
    status_stok = cek_status_stok(stok)
    
    if status_stok == "Stok Menipis":
        jumlah_barang_kritis += 1
        
    print(f"ID: {id_barang} | Nama: {nama_barang} | Stok: {stok} | Status: {status_stok}")
    
print("=================================")
print(f"Jumlah Barang Kritis: {jumlah_barang_kritis}")