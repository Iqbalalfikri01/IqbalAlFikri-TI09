#input
nama = input("masukan nama anda : ")
umur = input("masukkan umur anda : ")
tinggi = input("masukkan tinggi anda : ")

#logika
if int(tinggi) >= 90 :
    ket = "anda boleh bermain"
else :
    ket = "anda tidak boleh bermain"

#ouput
print("nama anda : ", nama)
print("umur anda :", umur)
print("tinggi anda :", tinggi)
print(ket)