text = input("Masukkan sebuah kata: ")
if any(vokal in text.lower() for vokal in 'aeiou'):
    print("Kata tersebut mengandung huruf vokal.")
else:
    print("Kata tersebut tidak mengandung huruf vokal.")