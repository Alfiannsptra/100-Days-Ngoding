# Membuat dictionary
siswa = {
    'nama': 'Alfian',
    'usia':21,
    'kelas': 'inf d'
}

# Mengakses nilai menggunakan kunci
print("Nama:", siswa['nama'])
print("Usia:", siswa['usia'])
print("Kelas:", siswa['kelas'])

# Menambahkan 
siswa['nilai_matematika'] = 90

# Mengubah nilai
siswa['usia'] = 24

# Menghapus 
del siswa['kelas']
