def pengulangan():
    Masukkan_bilangan_1_boy = int(input('bilangan 1 = '))
    Masukkan_Bilangan_2_girl = int(input('bilangan 2 = '))
    Masukkan_bilangan_3_sist =int(input('bilangan 3 = '))

    if Masukkan_bilangan_1_boy<Masukkan_Bilangan_2_girl and  Masukkan_bilangan_1_boy<Masukkan_bilangan_3_sist:
        if Masukkan_Bilangan_2_girl<Masukkan_bilangan_3_sist:
            print("Urutan bilangan dari yang terkecil adalah",Masukkan_bilangan_1_boy, Masukkan_Bilangan_2_girl, Masukkan_bilangan_3_sist)
        else:
            print("Urutan bilangan dari yang terkecil adalah",Masukkan_bilangan_1_boy,  Masukkan_bilangan_3_sist, Masukkan_Bilangan_2_girl)
    elif Masukkan_Bilangan_2_girl < Masukkan_bilangan_1_boy and Masukkan_Bilangan_2_girl < Masukkan_bilangan_3_sist:
        if Masukkan_bilangan_1_boy < Masukkan_bilangan_3_sist:
            print("Urutan bilangan dari yang terkecil adalah",Masukkan_Bilangan_2_girl, Masukkan_bilangan_1_boy, Masukkan_bilangan_3_sist)
        else:
            print("Urutan bilangan dari yang terkecil adalah",Masukkan_Bilangan_2_girl, Masukkan_bilangan_3_sist, Masukkan_bilangan_1_boy)
    else:
        if Masukkan_bilangan_1_boy < Masukkan_Bilangan_2_girl:
            print("Urutan bilangan dari yang terkecil adalah",Masukkan_bilangan_3_sist,  Masukkan_bilangan_1_boy, Masukkan_Bilangan_2_girl)
        else:
            print("Urutan bilangan dari yang terkecil adalah",Masukkan_bilangan_3_sist, Masukkan_Bilangan_2_girl, Masukkan_bilangan_1_boy)
            

  
pengulangan()




