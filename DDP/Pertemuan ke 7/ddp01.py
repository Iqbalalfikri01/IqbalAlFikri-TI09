# Declaring Bensin, Jarak Tempuh Bensin, Kota
pLite = 10000
pMax = 14000
pTurbo = 17000
# Jarak Tempuh Bensin / liter
jTempuhPLite = 12
jTempuhPMax = 13
jTempuhPTurbo = 13.5
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
jBensin = input('Jenis Bensin Yang Anda gunakan (all-lowercase): ')
kotaTuju = input('Kota Yang Anda Tuju (all-lowercase): ')

if (kotaTuju == 'jakarta'):
    kotaTuju = jakarta
elif (kotaTuju == 'bekasi'):
    kotaTuju = bekasi
elif (kotaTuju == 'depok'):
    kotaTuju = depok
elif (kotaTuju == 'tangerang'):
    kotaTuju = tangerang
elif (kotaTuju == 'bogor'):
    kotaTuju = bogor

if (jBensin == 'pertalite'):
    hasilPakai = kotaTuju / jTempuhPLite
    totalHarga = hasilPakai * pLite
elif (jBensin == 'pertamax'):
    hasilPakai = kotaTuju / jTempuhPMax
    totalHarga = hasilPakai * pMax
elif (jBensin == 'pertamax turbo'):
    hasilPakai = kotaTuju / jTempuhPTurbo
    totalHarga = hasilPakai * pTurbo
else:
    print(f'invalid Jenis Bensin : {jBensin}')

# Print the Input/Output
print(f' - Nama Kendaraan : {namaKen} \n - Jenis Bensin : {jBensin} \n - Kota Yang Dituju {kotaTuju} \n - Total Bensin Yang Digunakan : {hasilPakai} Liter \n - Total Harga Bensin Yang Digunakan : {totalHarga} Rupiah.')
