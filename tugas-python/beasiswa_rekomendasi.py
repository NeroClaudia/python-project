def rekomendasi_beasiswa(data_mahasiswa):
    total = 0
    for mahasiswa in data_mahasiswa:
        total += mahasiswa["nilai_evaluasi"]
    rata_rata = total / len(data_mahasiswa)

    print("=== REKOMENDASI PENERIMA BEASISWA ===")
    print(f"Rata-rata nilai evaluasi: {rata_rata:.2f}")
    print("===========================")

    ada_rekomendasi = False
    for mahasiswa in data_mahasiswa:
        if (mahasiswa["nilai_evaluasi"] > rata_rata and mahasiswa["prestasi"] >= 2):
            print(f"Nama: {mahasiswa["nama"]}")
            print(f"IPK: {mahasiswa["ipk"]}")
            print(f"Nilai Screening: {mahasiswa["screening"]}")
            print(f"Jumlah Prestasi: {mahasiswa["prestasi"]}")
            ada_rekomendasi = True
    if not ada_rekomendasi:
        print("Tidak ada mahasiswa rekomendasi")
