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
    if jumlah > 50:
        return 0.05
    elif jumlah > 20:
        return 0.03
    elif jumlah > 10:
        return 0.02
    elif jumlah > 5:
        return 0.01
    else:
        return 0 

def hitung_bonus():
    if jumlah > 50:
        return "Anda mendapatkan bonus: 5 barang gratis!"
    elif jumlah > 20:
        return "Anda mendapatkan bonus: 2 barang gratis!"
    elif jumlah > 10:
        return "Anda mendapatkan bonus: 1 barang gratis!"
    else:
        return "Tidak ada bonus."
    
diskon = hitung_diskon()
cashback = hitung_cashback()
bonus = hitung_bonus()
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
if jumlah > 5:
    print(f"Cashback: Rp{total_harga * cashback}")
else:    print("Cashback: Rp0")
print(f"Total Bayar: Rp{total_bayar}")
print(f"Bonus: {bonus}")