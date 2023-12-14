def kali_array(array1, array2):
    
    if len(array1) != len(array2):
        return "Panjang array tidak sama"

    hasil_array = [0] * len(array1)

    for i in range(len(array1)):
        hasil_array[i] = array1[i] * array2[i]

    return hasil_array
array_a = [1, 2, 3, 4]
array_b = [5, 6, 7, 8]

hasil = kali_array(array_a, array_b)
print("Hasil perkalian array:", hasil)
