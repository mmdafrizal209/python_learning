class User:
    def __init__(self, username):
        self.username = username
        self.photos = []

    def upload_photo(self, photo):
        self.photos.append(photo)
        print(f"{self.username} telah mengunggah foto: {photo}")

    def view_photos(self):
        if not self.photos:
            print(f"{self.username} belum mengunggah foto.")
        else:
            print(f"Foto yang diunggah oleh {self.username}:")
            for photo in self.photos:
                print(f"- {photo}")


class Instagram:
    def __init__(self):
        self.users = {}

    def create_account(self, username):
        if username in self.users:
            print("Username sudah ada. Silakan pilih username lain.")
        else:
            self.users[username] = User(username)
            print(f"Akun {username} telah dibuat.")

    def upload_photo(self, username, photo):
        if username in self.users:
            self.users[username].upload_photo(photo)
        else:
            print("Akun tidak ditemukan. Silakan buat akun terlebih dahulu.")

    def view_photos(self, username):
        if username in self.users:
            self.users[username].view_photos()
        else:
            print("Akun tidak ditemukan.")


def main():
    instagram = Instagram()

    while True:
        print("\n=== Menu Instagram ===")
        print("1. Buat Akun")
        print("2. Unggah Foto")
        print("3. Lihat Foto")
        print("4. Keluar")

        choice = input("Pilih opsi (1/2/3/4): ")

        if choice == '1':
            username = input("Masukkan username: ")
            instagram.create_account(username)

        elif choice == '2':
            username = input("Masukkan username: ")
            photo = input("Masukkan nama foto yang diunggah: ")
            instagram.upload_photo(username, photo)

        elif choice == '3':
            username = input("Masukkan username: ")
            instagram.view_photos(username)

        elif choice == '4':
            print("Terima kasih telah menggunakan aplikasi Instagram sederhana!")
            break

        else:
            print("Pilihan tidak valid! Harap pilih 1, 2, 3, atau 4.")


if __name__ == "__main__":
    main()