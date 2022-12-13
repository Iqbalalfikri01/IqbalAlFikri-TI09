def grade(nilai, nama, matkul):
    if nilai >= 85 and nilai <= 100 :
        print('Nama Mahasisawa : ', nama)
        print('Matakuliah : ', matkul)
        print('Nilai : ', nilai)
        print('Grade Nilai : A')
    elif nilai >= 75 and nilai <= 85 :
        print('Nama Mahasisawa : ', nama)
        print('Matakuliah : ', matkul)
        print('Nilai : ', nilai)
        print('Grade Nilai : B')
    elif nilai >= 60 and nilai <= 75 :
        print('Nama Mahasisawa : ', nama)
        print('Matakuliah : ', matkul)
        print('Nilai : ', nilai)
        print('Grade Nilai : C')
    else :
        print('Nama Mahasisawa : ', nama)
        print('Matakuliah : ', matkul)
        print('Nilai : ', nilai)
        print('Grade Nilai : D')
    
grade(97, 'Iqbal', 'ddp')
grade(60, 'puan', 'ddp')