def hitung_evaluasi(data_mahasiswa):
    for mahasiswa in data_mahasiswa:
        nilai_evaluasi = (mahasiswa["ipk"] * 20) + (mahasiswa["screening"] * 0.5) + (mahasiswa["prestasi"] * 10)
        mahasiswa["nilai_evaluasi"] = nilai_evaluasi
    return data_mahasiswa