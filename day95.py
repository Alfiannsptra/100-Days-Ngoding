import random

def tarik_kartu():
    jenis_kartu = ['Hati', 'Wajik', 'Keriting', 'Lingkaran']
    nilai_kartu = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    
    # Memilih secara acak jenis dan nilai kartu
    jenis = random.choice(jenis_kartu)
    nilai = random.choice(nilai_kartu)

    return f"Kartu yang Anda tarik: {nilai} {jenis}"

def main():
    while True:
        input("Tekan Enter untuk menarik kartu...")
        kartu_yang_ditarik = tarik_kartu()
        print(kartu_yang_ditarik)

main()
