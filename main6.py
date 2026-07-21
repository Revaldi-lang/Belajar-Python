# Data log mentah (List berisi kumpulan Tuple)
log_pengunjung = [
    ("Revaldi", "Lihat Nilai"),
    ("Fadjar", "Pengisian KRS"),
    ("Adam", "Pengisian KRS"),
    ("Dewi", "Lihat Jadwal"),
    ("Ahmad", "Lihat Nilai"),
    ("Rizky", "Pengisian KRS")
]

total_log = len(log_pengunjung) 

mahasiswa_unik = set()


for log in log_pengunjung:
    nama = log[0]  
    mahasiswa_unik.add(nama) 

pengisi_krs = []

for log in log_pengunjung:
    nama = log[0]
    menu = log[1] 
    
    if menu == "Pengisian KRS" and nama in pengisi_krs:
        continue
    elif menu == "Pengisian KRS":
        pengisi_krs.append(nama)
    elif menu == "Lihat Nilai":
        print(f"{nama} mengakses menu Lihat Nilai.")
    elif menu == "Lihat Jadwal":
        print(f"{nama} mengakses menu Lihat Jadwal.")
    else:
        print(f"{nama} mengakses menu {menu}.")

print("=== LAPORAN AKSES SISTEM ===")
print(f"Total Log Aktivitas: {total_log} kali akses.")
print(f"Daftar Mahasiswa yang Aktif Hari Ini: {mahasiswa_unik}")
print(f"Mahasiswa yang Melakukan Pengisian KRS: {pengisi_krs}")
print("=============================")