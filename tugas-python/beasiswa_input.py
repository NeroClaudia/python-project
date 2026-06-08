def input_mahasiswa():
    kondisi = False
    while kondisi == False:
        jumlah = int(input("Jumlah Mahasiswa: "))
        if (jumlah >= 2):
                data_mahasiswa = []
                for i in range(1, jumlah + 1):
                    nama_mahasiswa = input("Masukkan Nama Mahasiswa: ")
                    ipk = float(input("Masukkan IPK: "))
                    nilai_screening = float(input("Masukkan nilai screening: "))
                    jml_prestasi = int(input("Masukkan jumlah prestasi: "))

                    data_mahasiswa.append({
                        "nama": nama_mahasiswa,
                        "ipk": ipk,
                        "screening": nilai_screening,
                        "prestasi": jml_prestasi
                    })
                break
        else:
            print("Data mahasiswa minimal 2. Silahkan input ulang")
            
    return data_mahasiswa