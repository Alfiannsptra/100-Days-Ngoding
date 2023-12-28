status_lampu = input("Masukkan status lampu (merah/kuning/hijau): ")

if status_lampu.lower() == "merah":
    print("Berhenti!")
elif status_lampu.lower() == "kuning":
    print("Persiapkan diri, sebentar lagi hijau!")
elif status_lampu.lower() == "hijau":
    print("Anda dapat melanjutkan perjalanan.")
else:
    print("Status lampu tidak valid.")
