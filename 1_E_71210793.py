print("==== Kalkulator Akar dan Pangkat====")
print("Pilihan menu :")

print("1. Pangkat 2 (kuadrat)")
print("2. Pangkat 3 (Kubik)")
print("3. Akar Kuadrat")

menu_yang_dipilih = int(input("Masukan menu yang anda pilih :"))

if  menu_yang_dipilih ==1:
    perhitungan_pertama = int(input("Masukan bilangan yang mau di pangkatkan :"))
    rumus = perhitungan_pertama **2
    print("Hasil dari pemangkatan bilagan",perhitungan_pertama, "dengan 2 (kuadrat) adalah",rumus)

elif menu_yang_dipilih ==2:
    perhitungan_pertama = int(input("Masukan bilangan yang mau di pangkatkan :"))
    rumus = perhitungan_pertama **3
    print("Hasil dari pemangkatan bilagan",perhitungan_pertama, "dengan 3 (kubik) adalah",rumus)

elif menu_yang_dipilih ==3:
    perhitungan_pertama = int(input("Masukan bilangan yang mau di akarkan :"))
    rumus = perhitungan_pertama **(1/2)
    print("Hasil akar kuadrat dari bilangan",perhitungan_pertama,"adalah",rumus )
else:
    print("Pilihan menu yang dimasukkan tidak sesuai!")













