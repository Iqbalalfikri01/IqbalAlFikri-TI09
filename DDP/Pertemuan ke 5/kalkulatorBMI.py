print("")
print(" Program Menghitung Berat Badan Ideal")
print("")
 
#input
tinggibadan= input("Masukkan tinggi badan anda (dalam centimeter/cm) = ")

#rumus
tinggibadan2= (int(tinggibadan) - 100) * 10/100
beratideal= (int(tinggibadan) - 100) - int(tinggibadan2)

#output
print("Berat badan ideal anda adalah = ", beratideal, "kg")

print("")
print("Created By: Muhammad Fadhillah Iqbal Al-fikri TI-09")