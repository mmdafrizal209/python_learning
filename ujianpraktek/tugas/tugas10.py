notes = []

def add_note(note):
    notes.append(note)

def show_notes():
    for note in notes:
        print(note)

while True:
    note = input("Masukkan catatan (atau ketik 'exit' untuk keluar): ")
    if note.lower() == 'exit':
        break
    add_note(note)

print("Catatan Anda:")
show_notes()