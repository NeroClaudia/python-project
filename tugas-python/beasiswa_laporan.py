def tampilkan_data(data_mahasiswa):
    print("=== DAFTAR MAHASISWA ===")
    for mahasiswa in data_mahasiswa:
        print(f"Nama: {mahasiswa['nama']}")
        print(f"IPK: {mahasiswa['ipk']}")
        print(f"Nilai Screening: {mahasiswa['screening']}")
        print(f"Jumlah Prestasi: {mahasiswa['prestasi']}")
        print(f"Nilai Evaluasi: {mahasiswa['nilai_evaluasi']}")
        print("========================")