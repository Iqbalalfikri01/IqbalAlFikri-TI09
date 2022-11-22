#input
bilangan1 = int(input('masukan bilangan ke-1 = '))
bilangan2 = int(input('masukan bilangan ke-2 = '))
operasi = input('mmasukan operasi = ')

#rumus
if operasi == 'kali' :
    hasil = bilangan1*bilangan2

#output
print("bilangan pertama = ", bilangan1)
print("bilangan kedua = ", bilangan2)
print('pilihan operator = ', operasi)
print('Hasil operator ', bilangan1, "x", bilangan2 , "=", hasil)