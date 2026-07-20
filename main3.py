# Data log akses ke server utama
log_akses = [
    {"ip": "192.168.1.10", "user": "admin", "status": "Sukses"},
    {"ip": "10.0.0.5", "user": "staff_it", "status": "Gagal"},
    {"ip": "192.168.1.15", "user": "manager", "status": "Sukses"},
    {"ip": "198.51.100.7", "user": "unknown", "status": "Gagal"},
    {"ip": "10.0.0.5", "user": "staff_it", "status": "Sukses"}
]


def analisis_keamanan(ip_address, status_akses):
    if ip_address.startswith("198.51"):
        return "BERBAHAYA"
    elif status_akses == "Gagal":
        return "PERLU DIWASPADAI"
    else:
        return "AMAN"


total_ancaman = 0

print("=== SISTEM MONITORING KEAMANAN JARINGAN ===")

for log in log_akses:
    ip = log["ip"]
    user = log["user"]
    status = log["status"]
    
    analisis = analisis_keamanan(ip, status)
    
    if analisis in ["BERBAHAYA", "PERLU DIWASPADAI"]:
        total_ancaman += 1
    
    print(f"IP: {ip} | User: {user} | Analisis: {analisis}")
    
for log in log_akses:
    print(log["user"], "->", log["status"])

print("===========================================")
print(f"Total Ancaman Keamanan: {total_ancaman}")