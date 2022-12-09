hasilAkhir = [
    {'nama':'Reza','nilai':70},
    {'nama':'Ciut','nilai':63},
    {'nama':'Dian','nilai':80},
    {'nama':'Badu','nilai':40}
]

def lulusNilai(input):
    # Filter nilai siswa yang lulus
    siswaLulus = [i for i in input if i['nilai'] > 65]

    return siswaLulus

siswaLulus = lulusNilai(hasilAkhir)

for siswa in siswaLulus:
    print(f" {siswa['nama']} Lulus")