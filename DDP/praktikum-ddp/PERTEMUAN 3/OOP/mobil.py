class mobil:
    def __init__(self, tipe, roda, kecepatan, warna):
      self.tipe = tipe
      self.roda = roda
      self.kecepatan = kecepatan
      self.warna = warna

    def maju(self):
        print("Maju dengan kecepatan", self.kecepatan, "km/jam")

    def klakson(self):
        print("klakson")
    
    def belok(self, arah):
        print("Belok arah", arah)

# membuat object
mobil1 = mobil("Avanza", 4, 60, "putih");
print("warna mobil: ", mobil1.warna)
mobil1.maju()
mobil1.klakson()
mobil1.belok("kiri")