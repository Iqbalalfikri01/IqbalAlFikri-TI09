# Harga Bensin
pLite = 10.000
pTamax = 14.000
pTamaxturbo = 17.000
# Jarak Tempuh Bensin / Liter
jTempuhpLite = 12
jTempuhpTamax = 13
jTempuhpTamaxturbo = 13.5
# Kota Jarak Tempuh
jakarta = 20
bekasi = 35.7
depok = 5
tangerang = 99
bogor = 120.6
hasilPakai = 0
totalHarga = 0

# Variable input
namaKen = input('Kendaraan Yang Anda Pakai: ')
jBensin = input(' Jenis Bensin Yang Anda Gunakan : ')
kotaTuju = input('Kota Yang Anda Tuju : ')

if (kotaTuju == 'jakarta'):
    kotaDest = jakarta
elif (kotaTuju == 'bekasi'):
    kotaDest = bekasi
elif (kotaTuju == 'depok'):
    kotaDest = depok
elif (kotaTuju == 'tangerang'):
    kotaDest = tangerang
elif (kotaTuju == 'bogor'):
    kotaDest = bogor

if (jBensin == 'pertalite'):
    hasilPakai = kotaDest / jTempuhpLite
    totalHarga = hasilPakai * pLite
elif (jBensin == 'pertamax'):
    hasilPakai = kotaDest / jTempuhpTamax
    totalHarga = hasilPakai * pTamax
elif (jBensin == 'pertamax turbo'):
    hasilPakai = kotaDest / jTempuhpTamaxturbo
    totalHarga = hasilPakai * pTamaxturbo
else:
    print(f'invalid  Jenis Bensin : {jBensin}')

# output
print(f' - Nama Kendaraan : {namaKen} \n - Jenis Bensin : {jBensin} \n - Kota Yang Dituju {kotaTuju} \n - Total Bensin Yang Digunakan : {hasilPakai} Liter \n - Total Harga Bensin Yang Digunakan : {totalHarga} Rupiah.')