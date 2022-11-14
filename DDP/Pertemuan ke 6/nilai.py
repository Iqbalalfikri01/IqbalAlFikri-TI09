#input
nama = input("masukkan nama anda : ")
nilai = input("masukkan nilai anda : ")
kelas = input("masukkan kelas anda : ")

#rumus
if int(nilai) > 89 :
    ket = "istimewa"
elif int(nilai) > 69 :
    ket = "sangat bagus"
elif int(nilai) >59 :
    ket = "cukup"
else :
    ket = "gagal"

#output
print("nama anda : ", nama)
print("kelas anda : ", kelas)
print("nilai anda : ", nilai)
print(ket)
