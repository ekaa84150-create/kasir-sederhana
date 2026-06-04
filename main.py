nama = input("Masukkan Nama Pembeli: ")
barang = input("Masukkan Nama Barang: ")
jumlah = int(input("Masukkan Jumlah Barang: "))
harga = int(input("Masukkan Harga Barang: "))

member = input("Apakah Anda Member? (ya/tidak): ")
while member.lower() not in ["ya", "tidak"]:
    print("Input tidak valid. Silakan masukkan 'ya' atau 'tidak'.")
    member = input("Apakah Anda Member? (ya/tidak): ")

def hitung_diskon():
    if member.lower() == "ya":
        return 0.1 
    else:
        return 0  

def hitung_cashback():
    if jumlah > 5:
        return 0.05 
    else:
        return 0 
    
diskon = hitung_diskon()
cashback = hitung_cashback()
total_harga = jumlah * harga
total_diskon = total_harga * diskon
total_bayar = total_harga - total_diskon
print("\n--- Struk Pembelian ---")
print(f"Nama Pembeli: {nama}")
print(f"Nama Barang: {barang}")
print(f"Jumlah Barang: {jumlah}")
print(f"Harga Barang: Rp{harga}")
print(f"Total Harga: Rp{total_harga}")
print(f"Diskon: Rp{total_diskon}")
print(f"Total Bayar: Rp{total_bayar}")
if jumlah > 5:
    print(f"Cashback: Rp{total_harga * cashback}")
else:    print("Cashback: Rp0")