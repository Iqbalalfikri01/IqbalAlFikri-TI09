def balik_kalimat(isi):
  kata = isi.split(" ")
  putar = " ".join(reversed(kata))
  return putar

print("\nMembalik kalimat: \n")

print("saya mahasiswa Nurul Fikri", ":\n" + balik_kalimat("saya mahasiswa Nurul Fikri") + "\n")

print("saya prodi Teknik Informatika", ":\n" + balik_kalimat("saya prodi Teknik Informatika") + "\n")

print("Pemrograman Dasar Menyenangkan", ":\n" + balik_kalimat("Pemrograman Dasar Menyenangkan") + "\n")