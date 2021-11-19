daftar_siswa = str(input("Masukkan daftar siswa :"))
print("Daftar Siswa :", daftar_siswa.title().split(","))

siswa_tambahan = input("Masukan siswa yang ingin ditambahkan :")

if daftar_siswa in siswa_tambahan:
    print("Hasil penambahan pada daftar siswa :",daftar_siswa.title(),daftar_siswa, siswa_tambahan.upper())
else:
    print("Siswa atas nama",siswa_tambahan.upper(),"sudah berada dalam daftar siswa")




