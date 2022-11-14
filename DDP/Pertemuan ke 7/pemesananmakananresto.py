#Pemesanan makanan restoran

#input
nama = str(input("Masukan Nama Anda : "))
no_hp = int(input("Masukan No HP Anda : "))


pesanan = []
harga = []
total = 0

while True:
    print("Pesan Menu Apa? \n 1.Makanan \n 2.Minuman")
    pesan = int(input("Option : "))
    if pesan==1:
        print("----------------------------------------")
        print("            Menu Makanan")
        print("----------------------------------------")
        print("1.Nasi Goreng      Rp. 15.000")
        print("2.Mie Goreng       Rp. 12.000")
        print("3.Ayam Geprek      Rp. 18.000")
        hasil = int(input("Mau Pesan Apa? "))
        jumlah = int(input("Masukan Jumlah Pesanan Anda : "))
        if hasil==1 :
            pesanan.append("Nasi Goreng")
            harga.append(15000)
            total += 15000
        elif hasil==2 :
            pesanan.append("Mie Goreng")
            harga.append(12000)
            total += 12000
        elif hasil==3 :
            pesanan.append("Ayam Geprek")
            harga.append(18000)
            total += 18000
        else :
            print("pesanan yang adan pilih tidak tersedia")
    elif pesan==2 :
        print("----------------------------------------")
        print("            Menu Minuman")
        print("----------------------------------------")
        print("1.Aneka Jus        Rp. 15.000")
        print("2.Soft Drink       Rp. 10.000")
        print("3.Sweet Ice Tea    Rp. 5.000")
        hasil = int(input("Mau Pesan Apa? "))
        jumlah = int(input("Masukan Jumlah Pesanan Anda : "))
        if hasil==1 :
            pesanan.append("Aneka Jus")
            harga.append(15000)
            total += 15000
        elif hasil==2 :
            pesanan.append("Soft Drink")
            harga.append(10000)
            total += 10000
        elif hasil==3 :
            pesanan.append("Sweet Ice Tea")
            harga.append(5000)
            total += 5000
        else :
            print("pesanan yang adan pilih tidak tersedia")
    else :
        print("kode yang anda masukan tidak valid")

    lanjut = input("Tambah Pesanan (y/t) ? ")
    if lanjut=="t" :
        print("")
        break


#output
print("========================================")
print("Nama Pembeli : ", nama)
print("No HP Pembeli : ", no_hp)
print("Menu yang dipesan : ", pesanan)
print("harga : ", harga)
print("Jumlah Pesanan : ", jumlah)
print("Harga yang harus anda bayar : Rp.", total * jumlah)
