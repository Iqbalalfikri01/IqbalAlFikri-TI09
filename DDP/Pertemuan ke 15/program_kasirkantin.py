class Kasir:
  def __init__(self, nama, uang):
    self.nama = nama
    self.uang = uang

  # Method untuk menampilkan menu makanan
  def menu_makanan(self):
    print("Menu Makanan:")
    print("1. Nasi Goreng \t Rp. 15000")
    print("2. Mie Goreng \t Rp. 10000")
    print("3. Ayam Goreng \t Rp. 20000")
    print("4. Soto \t Rp. 12000")
    print("5. Gado-gado \t Rp. 10000")

  # Method untuk menampilkan menu minuman
  def menu_minuman(self):
    print("Menu Minuman:")
    print("1. Teh \t\t Rp. 5000")
    print("2. Kopi \t Rp. 7000")
    print("3. Jus \t\t Rp. 8000")
    print("4. Milkshake \t Rp. 10000")
    print("5. Es Teler \t Rp. 12000")

  # Method untuk membeli makanan atau minuman
  def beli(self, menu, jumlah):
    # Dictionary yang menyimpan harga dari setiap menu makanan atau minuman
    harga = {
      "Nasi Goreng": 15000,
      "Mie Goreng": 10000,
      "Ayam Goreng": 20000,
      "Soto": 12000,
      "Gado-gado": 10000,
      "Teh": 5000,
      "Kopi": 7000,
      "Jus": 8000,
      "Milkshake": 10000,
      "Es Teler": 12000
    }

    # Inisialisasi variabel total harga dengan 0
    total_harga = 0
    # Buat list untuk menyimpan daftar menu yang dibeli
    daftar_menu = []

    # Iterasi setiap menu yang diminta
    for i in range(len(menu)):
      # Cek apakah menu yang diminta tersedia di dictionary harga
      if menu[i] in harga:
        # Hitung total harga dari pembelian
        total = harga[menu[i]] * jumlah[i]
        # Tambahkan total harga ke variabel total_harga
        total_harga += total
        # Tambahkan menu ke daftar menu yang dibeli
        daftar_menu.append(f"{menu[i]} ({jumlah[i]} x Rp. {harga[menu[i]]})")
      else:
        # Jika menu yang diminta tidak tersedia di dictionary harga, tampilkan pesan error
        print("Maaf, menu yang Anda minta tidak tersedia di kantin kami.")

    # Cek apakah uang yang dimiliki cukup untuk membayar pembelian
    if self.uang >= total_harga:
      # Kurangi uang yang dimiliki dengan total harga pembelian
      self.uang -= total_harga
      # Tampilkan struk pembelian
      print("Terima kasih sudah berbelanja di kantin kami!")
      print("Nama:", self.nama)
      print("Menu:", ', '.join(daftar_menu))
      print("Total Harga: Rp.", total_harga)
      print("Uang yang tersisa: Rp.", self.uang)
    else:
      # Jika uang tidak cukup, tampilkan pesan error
      print("Maaf, uang yang Anda miliki tidak cukup untuk membayar pembelian.")

# Buat objek dari class Kasir
konsumen1 = Kasir("IqbalAlFikri", 50000)

# Tampilkan menu makanan
konsumen1.menu_makanan()

# Tampilkan menu minuman
konsumen1.menu_minuman()

# Konsumen membeli 1 Nasi Goreng dan 2 Kopi
konsumen1.beli(["Nasi Goreng", "Kopi", "Kopi"], [1, 2, 2])