
import tkinter as tk
from tkinter import *
import random

# Not: matris yamuk gibi gözükebilir gemileri str tanımladığım için öyle gözüküyor indisleri sayarsanız yamuk değil
oyun = 1
while (oyun == 1):

    print("Amiral battı oyununa hoşgeldiniz :)")
    secim = int(input("\nGizli modda oyun oynamak için 1'e,gemilerin yerini görmek için 0'a basınız:"))
    m_boyut = int(input("Kare oyun alanının boyutunu giriniz:"))

    atıs_hakkı = (m_boyut * m_boyut) // 3

    matris_gizli = [["?" for y in range(m_boyut)] for x in range(m_boyut)]

    matris = [[0 for y in range(m_boyut)] for x in range(m_boyut)]

    for x in range(m_boyut):
        for y in range(m_boyut):
            matris[x][y] = random.randint(0, 9)  # matrise 0 ile 9 arasında rastege rakam ata

    gemiler = ["#", "##", "###", "####"]

    gemilerX = []
    gemilerY = []

    for i in range(len(gemiler)):
        rx = random.randint(0,
                            m_boyut - 4)  # 1 den 20 ye kadardı şimdi 4 çıkarırsam matrisin sınırlarını aşmamış olacağım
        ry = random.randint(0, m_boyut - 4)

        ran = [1, 0]  # bu gemilerin random olarak dikey veya yatay yerleştirilmesinde belirleyici olacak
        a = random.choice(ran)  # "ran" listesinden random olarak bir değer seç

        for j in range(len(gemiler[i])):

            if (a == 0):
                matris[rx][ry + j] = gemiler[i][j]  # random olarak seçtiğin değer 0 ise gemiyi dikey yerleştir
                gemilerX.append(rx)
                gemilerY.append(ry + j)

            elif (a == 1):
                matris[rx + j][ry] = gemiler[i][j]  # 1 ise yatay yerleştir
                gemilerX.append(rx + j)
                gemilerY.append(ry)

    # print("\n\n{}\n{}\n\n\n".format(gemilerX,gemilerY)) gemilerX i ve gemilerY yi yazdırırsanız x de x i y de y yi görürsünüz

    atanılan_yerler = []

    for i in range(len(gemilerX)):  # gemilerX in de gemilerY nin de boyutu aynı
        atanılan_yerler.append(gemilerX[i])
        atanılan_yerler.append(gemilerY[i])

    #print("{}\n\n".format(atanılan_yerler)) #Burayı aktif ederseniz gemilerin indislerini görürsünüz

    for i in range(m_boyut):
        print(matris_gizli[i])

    sayac = 0
    bitti = 0
    a = 1  # kullanıcı çıkmak istemediği ya da oyun bitmediği sürece a=1 kalacak

    bir_birimlik_gemi = 0
    iki_birimlik_gemi = 0
    uc_birimlik_gemi = 0
    dort_birimlik_gemi = 0  # 2,3 ve 4 birimlik gemilerde birim sayısını ölçmek için kullanılacak sayaclar

    vurus = 0  # kullanıcı aynı yere 1 den fazla kez vurduğunda vuruş değerini sayacak

    vurulan_yerler = []  # kullanıcının girdiği yerleri tutacak
    s = 0  # hiçbir gemiyi vuramazsa while döngüsünden çıkmamı sağlayacak sayaç

    if (secim == 1):

        while (1):
            x = int(input("\nBir yer vur!\n\nVuracağın yerin x indisini gir:"))
            y = int(input("Vuracağın yerin y indisini gir:"))

            for i in range(0, len(vurulan_yerler) - 1, 2):
                if (x == vurulan_yerler[i] and y == vurulan_yerler[i + 1]):
                    print("Aynı yeri birden fazla kez vuramazsınız")
                    vurus = 1  # tekrar aynı vuruşu yaparsa burayı 1 yap
                else:
                    vurus = 0  # farklı bir vuruşsa 0 a eşitleyip devam edecek

            if (vurus == 1):  # ve 1 ise başa dönsün alttaki döngüye giremesin
                continue

            for i in range(0, len(atanılan_yerler) - 1, 2):  # sadece x lere bak. y olanlar x in 1 fazlası

                if (x == atanılan_yerler[i] and y == atanılan_yerler[i + 1]):
                    print("Tebrikler bir gemi vurdunuz!")
                    atıs_hakkı -= 1
                    print("                                                 Kalan atış hakkı:{}".format(atıs_hakkı))
                    if (atıs_hakkı == 0):
                        print("Maalesef atış hakkın bitti.Oyunu kaybettin!")
                        break

                    vurulan_yerler.append(x)  # vurulan yerler listesine ekle..daha sonra karşılaştırma yapacağm
                    vurulan_yerler.append(y)  # aynı yeri 2 kere vurmuş mu karşılaştırılmasını yapacak

                    matris_gizli[x][y] = "x"

                    if (i == 0):
                        bir_birimlik_gemi = 1
                        if (bir_birimlik_gemi == 1):
                            print("Tebrikler 1 birimlik gemiyi batırdın!!")

                    if (i == 2 or i == 4):  # atanılan_yerler listesindeki x e bakacak
                        iki_birimlik_gemi += 1  # kaç kere vurduğumu belirleyecek sayaç
                        if (iki_birimlik_gemi == 2):
                            print("Tebrikler 2 birimlik gemiyi batırdın!!")

                    if (i == 6 or i == 8 or i == 10):  # atanılan_yerler listesindeki x e bakacak
                        uc_birimlik_gemi += 1  # kaç kere vurduğumu belirleyecek sayaç
                        if (uc_birimlik_gemi == 3):
                            print("Tebrikler 3 birimlik gemiyi batırdın!!")

                    if (i == 12 or i == 14 or i == 16 or i == 18):  # atanılan_yerler listesindeki x e bakacak
                        dort_birimlik_gemi += 1  # kaç kere vurduğumu belirleyecek sayaç
                        if (dort_birimlik_gemi == 4):
                            print("Tebrikler 4 birimlik gemiyi batırdın!!")

                else:
                    s += 1

                    if (s == 10):
                        print("\n\nMaalesef isabet ettiremediniz")
                        atıs_hakkı -= 1
                        print("                                                 Kalan atış hakkı:{}".format(atıs_hakkı))
                        if (atıs_hakkı == 0):
                            print("Maalesef atış hakkın bitti.Oyunu kaybettin!")
                            print("Matris böyle idi: \n")
                            for i in range(m_boyut):
                                print(matris[i])

                            bitti = 1
                            break
                        matris_gizli[x][y] = "*"
                        vurulan_yerler.append(x)
                        vurulan_yerler.append(y)
                        s = 0
            s = 0
            # for i in range(m_boyut):
            #   print(matris_gizli[i])
            if (bitti == 1):
                break

            if (
                    bir_birimlik_gemi == 1 and iki_birimlik_gemi == 2 and uc_birimlik_gemi == 3 and dort_birimlik_gemi == 4):
                # atıs hakkını zaten her seferinde çıkarmıştım yani toplam haktan yapılan atışlar çıkarılmış oldu
                print("Tebrikler tüm gemileri batırdınız :) !!!\n Puanınız:{} :)".format(atıs_hakkı))
                print("\n" * 5)
                break

        devam = int(input("Oyuna devam etmek için 1'e sonlandırmak için 0'a basınız:"))
        if (devam == 0):
            break




    elif (secim == 0):

        pencere = tk.Tk()
        # kodlar buaraya yazılır
        pencere.title("AMİRAL BATTI :)")
        pencere.geometry("500x500+200+100")
        pencere.configure(bg="grey")

        for i in range(m_boyut):
            yazı = Label(text=matris[i], font="Verdana 15")
            yazı.place(x=80, y=20 + (30 * i))

        pencere.mainloop()
