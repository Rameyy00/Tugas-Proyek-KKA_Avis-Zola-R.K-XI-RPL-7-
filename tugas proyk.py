from abc import ABC, abstractmethod
# ABSTRACT CLASS
class BarangElektronik(ABC):
    def __init__(self, nama, stok, harga_dasar):
        self.nama = nama
        self.__stok = stok
        self.__harga_dasar = harga_dasar

    def get_stok(self):
        return self.__stok

    def tambah_stok(self, jumlah):
        if jumlah < 0:
            print(f"Gagal update stok {self.nama}: Stok tidak boleh negatif ({jumlah})")
        else:
            self.__stok += jumlah
            print(f"Berhasil menambahkan stok {self.nama}: {jumlah} unit.")

    def _get_harga_dasar(self):
        return self.__harga_dasar

    @abstractmethod
    def tampilkan_detail(self):
        pass

    @abstractmethod
    def hitung_harga_total(self, jumlah):
        pass
# LAPTOP
class Laptop(BarangElektronik):
    def __init__(self, nama, stok, harga_dasar, processor):
        super().__init__(nama, stok, harga_dasar)
        self.processor = processor

    def tampilkan_detail(self):
        print(f"[LAPTOP] {self.nama} | Proc: {self.processor}")

    def hitung_harga_total(self, jumlah):
        pajak = 0.10 * self._get_harga_dasar()
        subtotal = (self._get_harga_dasar() + pajak) * jumlah
        return pajak, subtotal
# SMARTPHONE
class Smartphone(BarangElektronik):
    def __init__(self, nama, stok, harga_dasar, kamera):
        super().__init__(nama, stok, harga_dasar)
        self.kamera = kamera

    def tampilkan_detail(self):
        print(f"[SMARTPHONE] {self.nama} | Cam: {self.kamera}")

    def hitung_harga_total(self, jumlah):
        pajak = 0.05 * self._get_harga_dasar()
        subtotal = (self._get_harga_dasar() + pajak) * jumlah
        return pajak, subtotal

def proses_transaksi(daftar_barang):
    total = 0
    print("\n--- STRUK TRANSAKSI ---")

    for i, (barang, jumlah) in enumerate(daftar_barang, start=1):
        print(f"{i}. ", end="")
        barang.tampilkan_detail()

        harga = barang._get_harga_dasar()
        pajak, subtotal = barang.hitung_harga_total(jumlah)

        print(f"Harga Dasar: Rp {harga:,.0f} | Pajak: Rp {pajak:,.0f}")
        print(f"Beli: {jumlah} unit | Subtotal: Rp {subtotal:,.0f}\n")

        total += subtotal

    print(f"TOTAL TAGIHAN: Rp {total:,.0f}")
    print("-" * 30)

print("--- SETUP DATA ---")

laptop = Laptop("ROG Zephyrus", 5, 20000000, "Ryzen 9")
hp = Smartphone("iPhone 13", 3, 15000000, "12MP")

laptop.tambah_stok(10)
hp.tambah_stok(-5)
hp.tambah_stok(20)

keranjang = [
    (laptop, 2),
    (hp, 1)
]

proses_transaksi(keranjang)