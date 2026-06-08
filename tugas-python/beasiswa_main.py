import beasiswa_input as bi
import beasiswa_evaluasi as be
import beasiswa_laporan as bl
import beasiswa_ranking as br
import beasiswa_rekomendasi as bre

data = None

while True:
    print("=== MENU ===")
    print("1. Tampilkan data pendaftaran")
    print("2. Tampilkan peringkat mahasiswa")
    print("3. Tampilkan rekomendasi penerima beasiswa")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        data = bi.input_mahasiswa()
        data = be.hitung_evaluasi(data)
        bl.tampilkan_data(data)
    elif pilihan == "2":
        if data is None:
            print("Data kosong")
        else:
            data = br.ranking_mahasiswa(data)
            bl.tampilkan_data(data)
    elif pilihan == "3":
            bre.rekomendasi_beasiswa(data)


