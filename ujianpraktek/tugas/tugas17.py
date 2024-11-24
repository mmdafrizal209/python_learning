def tampilkan_puisi():
    puisi = """
    Di bawah sinar bulan purnama,
    Hatiku bergetar saat melihatmu,
    Setiap detik bersamamu adalah berharga,
    Cintaku padamu takkan pernah pudar.

    Kau adalah bintang di malam gelap,
    Cahaya yang menerangi jalanku,
    Bersama kita jalani hidup ini,
    Selamanya kau dan aku, satu jiwa.
    """
    print(puisi)

def alasan_mencintaimu():
    alasan = [
        "Karena senyummu membuat hariku lebih cerah.",
        "Karena kehadiranmu membuatku merasa lengkap.",
        "Karena setiap momen bersamamu adalah kenangan berharga.",
        "Karena kamu selalu mendukungku dalam setiap langkah.",
        "Karena hatiku bergetar setiap kali melihatmu."
    ]
    for i, a in enumerate(alasan, 1):
        print(f"{i}. {a}")

def main():
    print("Selamat datang di program Mencintaimu!")
    print("Apa yang ingin kamu lakukan?")
    print("1. Tampilkan puisi cinta")
    print("2. Tampilkan alasan mengapa aku mencintaimu")
    print("3. Keluar")

    while True:
        pilihan = input("Masukkan pilihan (1/2/3): ")

        if pilihan == '1':
            tampilkan_puisi()
        elif pilihan == '2':
            alasan_mencintaimu()
        elif pilihan == '3':
            print("Terima kasih! Semoga cintamu selalu bersemi.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


main()