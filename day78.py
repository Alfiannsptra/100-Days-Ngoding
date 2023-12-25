import random

def lempar_koin():
    hasil = random.choice(["kepala", "Ekor"])
    return hasil

hasil_pelemparan = lempar_koin()
print("Hasil: ", hasil_pelemparan)
