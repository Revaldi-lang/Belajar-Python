data_proyek = [
    {"kode": "PRJ-01", "nama": "Sistem ERP Rumah Sakit", "pendapatan": 150000000, "biaya": 90000000, "target_profit": 50000000},
    {"kode": "PRJ-02", "nama": "Aplikasi E-Commerce", "pendapatan": 80000000, "biaya": 85000000, "target_profit": 20000000},
    {"kode": "PRJ-03", "nama": "Revitalisasi Jaringan", "pendapatan": 200000000, "biaya": 140000000, "target_profit": 70000000},
    {"kode": "PRJ-04", "nama": "Data Analytics Dashboard", "pendapatan": 120000000, "biaya": 70000000, "target_profit": 40000000}
]


def hitung_performa_bisnis(pendapatan, biaya, target):
    profit_bersih = pendapatan - biaya
    if profit_bersih < 0:
        status = "RUGI / BEP BELUM TERCAPAI"
    elif profit_bersih >= target:
        status = "SUKSES TARGET"
    else:
        status = "UNTUNG (DI BAWAH TARGET)"
    
    return profit_bersih, status


total_keuntungan_bersih = 0
jumlah_proyek_sukses = 0

print("================= LAPORAN FINANSIAL PROYEK =================")

for proj in data_proyek:
    kode = proj["kode"]
    nama = proj["nama"]
    pend = proj["pendapatan"]
    biaya = proj["biaya"]
    target = proj["target_profit"]
    
    profit_bersih, status_proyek = hitung_performa_bisnis(pend, biaya, target)
    
    total_keuntungan_bersih += profit_bersih
    
    if status_proyek == "SUKSES TARGET":
        jumlah_proyek_sukses += 1
    
    print(f"Kode: {kode} | Nama: {nama} | Pendapatan: Rp{pend:,} | Biaya: Rp{biaya:,} | Profit Bersih: Rp{profit_bersih:,} | Status: {status_proyek}")

print("============================================================")
print(f"Total Keuntungan Bersih: Rp{total_keuntungan_bersih:,}")
print(f"Jumlah Proyek Sukses Target: {jumlah_proyek_sukses}")