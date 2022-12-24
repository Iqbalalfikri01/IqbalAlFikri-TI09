class Gempa:
    #member1 Variabel
    lokasi = ''
    skla = 0
    #meember2 konstruktor
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala
    #member3 method
    def dampak (self):
        if(self.skala < 2): ket = 'Tidak Terasa'
        elif(self.skala >= 2 and self.skala < 4): ket = 'Bagunan Retak-retak'
        elif(self.skala >= 4 and self.skala < 6): ket = 'Bagunan Roboh'
        else: ket = 'Bangunan roboh dan berpotensi tsunami'
        print(
            "Lokasi Gempa\t:",self.lokasi,
            "\nSkala\t\t:",self.skala,"richter"
            "\nDampak\t\t:",ket,
            "\n-----------------------------------"
            )