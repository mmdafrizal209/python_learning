def count_words(text):
    words = text.split()
    return len(words)

text = input("Masukkan teks: ")
print(f"Jumlah kata: {count_words(text)}")