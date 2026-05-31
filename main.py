nama = input("Masukkan Nama Pembeli: ")
barang = input("Masukkan Nama Barang: ")
jumlah = int(input("Masukkan Jumlah Barang: "))
harga = int(input("Masukkan Harga Barang: "))

member = input("Apakah Anda Member? (ya/tidak): ")
while member.lower() not in ["ya", "tidak"]:
    print("Input tidak valid. Silakan masukkan 'ya' atau 'tidak'.")
    member = input("Apakah Anda Member? (ya/tidak): ")

totalHarga = jumlah * harga
diskon = 0

if member.lower() == "ya":
    diskon += totalHarga * 0.10

if jumlah > 5:
    diskon += totalHarga * 0.05

totalBayar = totalHarga - diskon

print(f"Nama Pembeli: {nama}")
print(f"Nama Barang: {barang}")
print(f"Jumlah Barang: {jumlah}")
print(f"Harga Barang: {harga}")
print(f"Diskon: {diskon}")
print(f"Total Harga: {totalBayar}")