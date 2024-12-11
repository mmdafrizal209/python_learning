class Item:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

class Kasir:
    def __init__(self):
        self.keranjang = []

    def tambah_item(self, item):
        self.keranjang.append(item)
        print(f"{item.nama} telah ditambahkan ke keranjang.")

    def hitung_total(self):
        total = sum(item.harga for item in self.keranjang)
        return total

    def cetak_struk(self):
        print("\n=== Struk Belanja ===")
        for item in self.keranjang:
            print(f"{item.nama}: Rp {item.harga:.2f}")
        total = self.hitung_total()
        print(f"Total: Rp {total:.2f}")
        print("======================")

def main():
    kasir = Kasir()

    while True:
        print("\n=== Menu Kasir ===")
        print("1. Tambah Item")
        print("2. Hitung Total")
        print("3. Cetak Struk")
        print("4. Keluar")

        pilihan = input("Pilih opsi (1/2/3/4): ")

        if pilihan == '1':
            nama_item = input("Masukkan nama item: ")
            try:
                harga_item = float(input("Masukkan harga item: Rp "))
                item = Item(nama_item, harga_item)
                kasir.tambah_item(item)
            except ValueError:
                print("Harga tidak valid! Harap masukkan angka.")

        elif pilihan == '2':
            total = kasir.hitung_total()
            print(f"Total belanja saat ini: Rp {total:.2f}")

        elif pilihan == '3':
            kasir.cetak_struk()

        elif pilihan == '4':
            print("Terima kasih telah menggunakan sistem kasir!")
            break

        else:
            print("Pilihan tidak valid! Harap pilih 1, 2, 3, atau 4.")

if __name__ == "__main__":
    main()