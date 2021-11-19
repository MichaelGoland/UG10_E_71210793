print("Suhu Tubuh")

suhu_tubuh = (float(input("Masukan suhu tubuh Anda: ")))

suhu_normal = 37

if suhu_tubuh > 50:
    print("Anda bukan Manusia:)")
elif 37.6 <= suhu_tubuh <= 50:
    print("Anda demam! Jangan berpergian ke tempat fasilitas umum.")
elif 32<= suhu_tubuh <= 37.5:
    print("Suhu Anda normal!")
elif suhu_tubuh < 32:
    print("Anda kedinginan! Silahkan cari sesuatu yang hangat")



