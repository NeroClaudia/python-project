def ranking_mahasiswa(data_mahasiswa):
    n = len(data_mahasiswa)
    for i in range(n):
        for j in range(n - i - 1):
            if (data_mahasiswa[j]["nilai_evaluasi"] < data_mahasiswa[j + 1]["nilai_evaluasi"]):
                temp = data_mahasiswa[j]
                data_mahasiswa[j] = data_mahasiswa[j + 1]
                data_mahasiswa[j + 1] = temp
    return data_mahasiswa
                