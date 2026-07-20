# Data transaksi penjualan toko online
data_penjualan = [
    {"id_transaksi": "TRX001", "produk": "Keyboard Kerja", "total_harga": 450000},
    {"id_transaksi": "TRX002", "produk": "Monitor Gaming", "total_harga": 2500000},
    {"id_transaksi": "TRX003", "produk": "Mouse Wireless", "total_harga": 150000},
    {"id_transaksi": "TRX004", "produk": "Kursi Ergonomis", "total_harga": 1800000},
    {"id_transaksi": "TRX005", "produk": "Mousepad Deskmat", "total_harga": 200000}
]

def cek_kategori_transaksi(harga):
    if harga >= 500000:
        return "Transaksi Besar"
    else:
        return "Transaksi Normal"

total_pendapatan = 0

print("=== LAPORAN PENJUALAN HARIAN ===")

for trx in data_penjualan:
    id_trx = trx["id_transaksi"]
    produk = trx["produk"]
    harga = trx["total_harga"]
    
    kategori = cek_kategori_transaksi(harga)
    
    total_pendapatan += harga
    
    print(f"ID: {id_trx}, Produk: {produk}, Harga: Rp{harga:,}, Kategori: {kategori}")

print("=================================")
print(f"Total Pendapatan: Rp{total_pendapatan:,}")