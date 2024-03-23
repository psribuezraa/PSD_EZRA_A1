def data_mahasiswa():
    jumlah_mahasiswa = int(input("Masukan jumlah mahasiswa: "))
    data_mahasiswa = []

    for i in range(jumlah_mahasiswa):
        nim = input(f"Masukan nim mahasiswa ke-{i+1} : ")
        nama = input(f"Masukan nama mahasiswa ke-{i+1}: ")

        nilai_ujian = []
        jmlh_ujian = int(input(f"Masukan jumlah ujian mahasiswa: "))

        for j in range(jmlh_ujian):
            nilai = int(input(f"Masukan nilai ujian ke-{j+1}: "))
            nilai_ujian.append(nilai)
        
        rata_rata_ujian = sum(nilai_ujian) / jmlh_ujian
        data_mahasiswa.append((nim, nama, rata_rata_ujian))

    for data in data_mahasiswa:
        print("=" * 20)
        print("Nama: ", data[1])
        print("NIM: ", data[0])
        print("Rata-rata nilai: ", data[2])

data_mahasiswa()