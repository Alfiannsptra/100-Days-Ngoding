pencapaian = 0
hari = 1

while hari <= 100:
    print(f"Hari ke-{hari}: Apakah Anda coding hari ini? (y/n)")
    jawaban = input().lower()

    if jawaban == 'y':
        pencapaian += 1
        print("Selamat! Anda telah coding hari ini.")
    elif jawaban == 'n':
        print("Terus semangat! Tetap konsisten dalam perjalanan coding Anda.")

    hari += 1

print(f"\nAnda telah berhasil coding selama {pencapaian} hari dari 100 hari.")
