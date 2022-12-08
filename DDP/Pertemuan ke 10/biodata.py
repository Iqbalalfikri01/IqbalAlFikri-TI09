#rumus
def bio(nama,alamat,tLahir,umur,tb,bmi) :
    bmi = str((int(tb) - 100)-((int(tb)- 100) * 0.10))
    print("Pekenalkan nama saya "+ nama)
    print("Saya tinggal di kota "+ alamat)
    print("Saya lahir pada tanggal "+ tLahir)
    print("Dan saya berumur "+ umur + " tahun")
    print("Saya memiliki tinggi badan "+ tb + " cm")
    print("Dan saya mempunyai berat badan ideal "+ bmi + " kg")

#output
bio("Iqbal","Depok","01 Juli 2004","18","170","55")