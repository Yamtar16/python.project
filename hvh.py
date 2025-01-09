import random


player_name = input("Kahramanınızın Adını Giriniz : ")
ensturman = input("enstürman adı giriniz: ")


class Karakter:
    def __init__(self, ad, can, guc, cevik, dayan):
        self.adi = ad
        self.cani = can
        self.guc = guc
        self.cevik = cevik
        self.dayan = dayan


class Oyuncu(Karakter):
    def __init__(self, ad, enstu, para=10, seviye=1, tecrube=0, can=100, tokluk=100, hijyen=100, eglence=100, uyku=100,guc=1, cevik=1, dayan=1, karizma=1, toplayicilik=1):

        super().__init__(ad, can, guc, cevik, dayan)
        self.ensturman = enstu
        self.para = para
        self.seviye = seviye
        self.tecrube = tecrube
        self.tokluk = tokluk
        self.hijyen = hijyen
        self.eglence = eglence
        self.uyku = uyku
        self.karizma = karizma
        self.toplayicilik = toplayicilik


haydut1 = Karakter('LVL1 Haydut', 100, random.randint(1, 5), random.randint(1, 5), random.randint(1, 5))

haydut2 = Karakter('LVL2 Haydut', 70, random.randint(6, 10), random.randint(6, 10), random.randint(6, 10))

haydut3 = Karakter('LVL3 Haydut', 90, random.randint(11, 15), random.randint(11, 15), random.randint(11, 15))

oyuncu1 = Oyuncu(player_name, ensturman, )



class Anamenu:
    def __init__(self):

        self.anamenulist = ["1. Kamp alanına git", "2. Şifahaneye git.", "3. Hana git.", "4. Maceraya atıl.",
                            "5. Seviye atla.", "6. Durumu göster.", "0. Oyundan çık."]

    def print_anamenu(self):



        if 30 <= oyuncu1.tokluk <= 10:
            print("Karakterin Açlıktan Başı Dönüyor Acilen Yemek Yemelisin!!")
        if oyuncu1.tokluk <= 0:
            print(oyuncu1.adi + " Kaya Kenarında Ölü Bulundu")
            gameover()
        if oyuncu1.uyku == 10:
            print("Karakterin Çok Uykusu Geldi.Uyumazsan Yol Kenarında Bayılacaksın ")
        if oyuncu1.uyku == 0:
            print("Karakterin Uykusuzluktan Bayıldı. Hırsızlar Cebinden 5 Altın Çaldı")
            oyuncu1.para -= 5
        if oyuncu1.hijyen == 0:
            print("Çok Kötü Kokuyorsun İnsanlar Senden Kaçıyor")
        if oyuncu1.eglence == 0:
            print("Canın Çok Sıkıldı.Unutma Böyle Devam Ederse Psikolojin Bozulacak")

        for i in self.anamenulist:
            print(i)

        oyuncu1.cani = min(oyuncu1.cani, 100)
        oyuncu1.tokluk = min(oyuncu1.tokluk, 100)
        oyuncu1.hijyen = min(oyuncu1.hijyen, 100)
        oyuncu1.eglence = min(oyuncu1.eglence, 100)
        oyuncu1.uyku = min(oyuncu1.uyku, 100)
        oyuncu1.cani = max(oyuncu1.cani, 0)
        oyuncu1.tokluk = max(oyuncu1.tokluk, 0)
        oyuncu1.hijyen = max(oyuncu1.hijyen, 0)
        oyuncu1.eglence = max(oyuncu1.eglence, 0)
        oyuncu1.uyku = max(oyuncu1.uyku, 0)
        oyuncu1.guc = min(oyuncu1.guc,25)
        oyuncu1.dayan =min(oyuncu1.dayan,25)
        oyuncu1.cevik = min(oyuncu1.cevik,25)
        oyuncu1.karizma =min(oyuncu1.karizma,25)
        oyuncu1.toplayicilik = min(oyuncu1.toplayicilik,25)

        whatyoudo = input("ne yapmak istersiniz?: ")

        try:
            whatyoudo = int(whatyoudo)
        except ValueError:
            print("lütfen Düzgün Sayı Giriniz")
            anamenu1.print_anamenu()




        if int(whatyoudo) == 0:
            print("oyundan çıkış yapılıyor.")
        elif int(whatyoudo) == 1:
            kampalani1.print_kampalani()
        elif int(whatyoudo) == 2:
            sifahane1.print_sifahane()
        elif int(whatyoudo) == 3:
            han1.print_han()
        elif int(whatyoudo) == 4:
            macera1.print_macera()
        elif int(whatyoudo) == 5:
            seviyeatla1.seviyeatla()
        elif int(whatyoudo) == 6:
            ozellikgoster1.ozellikgosterme1()
        else:
            print("Lütfen 0 İle 6 Arasında Bir Sayı Giriniz")
            anamenu1.print_anamenu()


class Kampalani:
    def __init__(self):
        self.kampalanilist = ["1. Kamp ateşinin başında çalgı çal.", "2. Nehirde yıkan.", "3. Çadırına girip uyu.",
                              "4. Köy meydanına dön"]

    def print_kampalani(self):

        for i in self.kampalanilist:
            print(i)

        whatyoudo1 = input("Kamp Alanında Ne yapmak İstersiniz :")

        try:
            whatyoudo1 = int(whatyoudo1)
        except ValueError:
            print("Lütfen Geçerli Değer Giriniz")
            kampalani1.print_kampalani()

        if int(whatyoudo1) == 1:
            oyuncu1.eglence += 20
            oyuncu1.tecrube += 10
            oyuncu1.tokluk -= 10
            oyuncu1.hijyen -= 10
            oyuncu1.uyku -= 10

            anamenu1.print_anamenu()

        elif int(whatyoudo1) == 2:
            oyuncu1.hijyen = 100
            oyuncu1.eglence -= 10
            oyuncu1.tokluk -= 10
            oyuncu1.uyku -= 10

            anamenu1.print_anamenu()

        elif int(whatyoudo1) == 3:
            oyuncu1.uyku = 100
            oyuncu1.eglence -= 10
            oyuncu1.hijyen -= 10
            oyuncu1.tokluk -= 10

            anamenu1.print_anamenu()

        elif int(whatyoudo1) == 4:

            anamenu1.print_anamenu()
        else:
            print("Geçerli Sayıdaki Sayıları Giriniz")
            kampalani1.print_kampalani()


class Sifahane:
    def __init__(self):
        self.sifahanelist = ["1. Şifacıdan yaralarını sarmasını iste.", "2. Şifacıdan merhem yapıp sürmesini iste.",
                             "3. Köy meydanına dön."]

    def print_sifahane(self):

        for i in self.sifahanelist:
            print(i)
        whatyoudo2 = input("Şifahanede Ne Yapmak İstersiniz :")

        try:
            whatyoudo2 = int(whatyoudo2)
        except ValueError:
            print("lütfen Düzgün Sayı Giriniz")
            sifahane1.print_sifahane()

        if int(whatyoudo2) == 1:
            oyuncu1.cani += 20
            oyuncu1.eglence -= 10
            oyuncu1.tokluk -= 10
            oyuncu1.uyku -= 10
            oyuncu1.hijyen -= 10

            anamenu1.print_anamenu()

        elif int(whatyoudo2) == 2:
            oyuncu1.cani += 50
            oyuncu1.eglence -= 10
            oyuncu1.tokluk -= 10
            oyuncu1.uyku -= 10
            oyuncu1.hijyen -= 10

            anamenu1.print_anamenu()

        elif int(whatyoudo2) == 3:
            anamenu1.print_anamenu()
        else:
            print("Geçerli Sayıdaki Sayıları Giriniz")
            sifahane1.print_sifahane()


class Han:
    def __init__(self):
        self.hanlist = ["1. Yiyecek satın al ve ye.", "2. İçecek satın al, iç ve eğlen.",
                        "3. Enstrüman çal ve şarkı söyle.", "4. Köy meydanına dön."]

    def print_han(self):

        for i in self.hanlist:
            print(i)
        whatyoudo3 = input("Handa Ne Yapmak İstersiniz :")

        try:
            whatyoudo3 = int(whatyoudo3)
        except ValueError:
            print("lütfen Düzgün Sayı Giriniz")
            han1.print_han()

        if int(whatyoudo3) == 1:
            if oyuncu1.para >= 10:
                oyuncu1.para -= 10
                oyuncu1.tokluk += 50
                oyuncu1.eglence -= 10
                oyuncu1.tokluk -= 10
                oyuncu1.uyku -= 10
                oyuncu1.hijyen -= 10
                anamenu1.print_anamenu()
            else:
                print("Hancı Paran Olmadığı İçin Seninle Dalga Geçti.Para Kazanıp Tekrar Gel")
                anamenu1.print_anamenu()


        elif int(whatyoudo3) == 2:
            if oyuncu1.para >= 5:
                oyuncu1.para -= 5
                oyuncu1.tokluk += 10
                oyuncu1.eglence += 50
                oyuncu1.tokluk -= 10
                oyuncu1.uyku -= 10
                oyuncu1.hijyen -= 10
                anamenu1.print_anamenu()
            else:
                print("Hancı Paran Olmadığı İçin Seninle Dalga Geçti.Para Kazanıp Tekrar Gel")
                anamenu1.print_anamenu()


        elif int(whatyoudo3) == 3:
            if oyuncu1.hijyen == 0:
                print("Handakiler Kokundan Rahatsız oldular.Buldukları Herşeyi Sana Fırlatıp Yuhaladılar")
            else:
                oyuncu1.eglence += 10
                oyuncu1.tecrube += 20
                oyuncu1.para += 10

                oyuncu1.tokluk -= 10
                oyuncu1.uyku -= 10
                oyuncu1.hijyen -= 10


        elif int(whatyoudo3) == 4:
            pass
        else:
            print("Geçerli Sayıdaki Sayıları Giriniz")
            han1.print_han()

        anamenu1.print_anamenu()


class Macera:
    def __init__(self):
        self.maceralist = ["1. Yakın çevreden şifalı bitki topla ve avlan.", "2. Ormanı keşfe çık (kolay).",
                           "3. Kayalıkları keşfe çık (orta).", "4. Vadiyi keşfe çık (zor).", "5. Köy meydanına dön."]

    def print_macera(self):

        for i in self.maceralist:
            print(i)
        whatyoudo4 = input("Macerada Ne Yapmak İstersiniz :")

        try:
            whatyoudo4 = int(whatyoudo4)
        except ValueError:
            print("lütfen Düzgün Sayı Giriniz")
            macera1.print_macera()

        ihtimal = random.randint(0, 100)
        ihtimal2 = random.randint(0, 100)
        ihtimal3 = random.randint(0, 100)
        if int(whatyoudo4) == 1:
            if ihtimal <= oyuncu1.toplayicilik * 4:
                oyuncu1.cani += 10
                print("Şifalı Bitki Buldun")
            else:
                print("Malesef Bitki Bulamadın")

            if ihtimal2 <= oyuncu1.toplayicilik * 4:
                oyuncu1.tokluk += 20
                print("Ormanda Meyve Buldun")
            else:
                print("Meyve Bulamadın")
            if ihtimal3 <= oyuncu1.toplayicilik * 2:
                oyuncu1.tokluk += 50
                print("Oyuncu Avlandı")
            else:
                print("Av Bulamadın")
            oyuncu1.eglence -= 10
            oyuncu1.tokluk -= 10
            oyuncu1.uyku -= 10
            oyuncu1.hijyen -= 10
            anamenu1.print_anamenu()
        elif int(whatyoudo4) == 2:

            if oyuncu1.cevik > haydut1.cevik:
                oncekarakter()



            elif haydut1.cevik > oyuncu1.cevik:
                oncehaydut()


            else:
                baslayacak = random.randint(1, 2)
                if baslayacak == 1:
                    oncekarakter()
                if baslayacak == 2:
                    oncehaydut()
        elif int(whatyoudo4) == 3:

            if oyuncu1.cevik > haydut2.cevik:
                oncekarakterorta()
            elif haydut2.cevik > oyuncu1.cevik:
                oncehaydutorta()
            else:
                baslayacak = random.randint(1, 2)
                if baslayacak == 1:
                    oncekarakterorta()
                if baslayacak == 2:
                    oncehaydutorta()
        elif int(whatyoudo4) == 4:

            if oyuncu1.cevik > haydut3.cevik:
                oncekarakterzor()
            elif haydut3.cevik > oyuncu1.cevik:
                oncehaydutzor()
            else:
                baslayacak = random.randint(1, 2)
                if baslayacak == 1:
                    oncekarakterzor()
                if baslayacak == 2:
                    oncehaydutzor()
        elif int(whatyoudo4) == 5:
            anamenu1.print_anamenu()
        else:
            print("Geçerli Sayıdaki Sayıları Giriniz")
            macera1.print_macera()


class Seviyeatla:
    def __init__(self):
        pass

    def seviyeatla(self):

        if oyuncu1.tecrube >= 100:
            print("Seviye Atladınız Tebrikler! Şimdi 3 Özelliğinizi geliştirin")
            oyuncu1.seviye += 1
            beceripuani = 3
            while beceripuani > 0:
                print("  Güçünüzü Geliştirmek İçin 1 Tuşuna Basınız")
                print("  Çevikliğinizi Geliştirmek İçin 2 Tuşuna Basınız")
                print("  Dayanıklılığınız Geliştirmek İçin 3 Tuşuna Basınız")
                print("  Karizmanızı Geliştirmek İçin 4 Tuşuna Basınız")
                print("  Toplayıcılığınızı Geliştirmek İçin 5 Tuşuna Basınız")

                tercih = input("Geliştirmek İstediğiniz Özelliği Giriniz")

                try:
                    tercih = int(tercih)
                except ValueError:
                    print("Geçersiz Tercih Yaptınız Lütfen Düzgün Sayı Giriniz")
                    continue

                if 1 <= tercih <= 5:
                    if tercih == 1:
                        oyuncu1.guc += 1
                        print("Güçünüz 1 Puan Arttırıldı")
                        beceripuani -= 1
                    elif tercih == 2:
                        oyuncu1.cevik += 1
                        print("Çevikliğiniz 1 Puan Arttırıldı")
                        beceripuani -= 1
                    elif tercih == 3:
                        oyuncu1.dayan += 1
                        print("Dayanıklılığınız 1 Puan Arttırıldı")
                        beceripuani -= 1
                    elif tercih == 4:
                        oyuncu1.karizma += 1
                        print("Karizmanız 1 Puan Arttırıldı")
                        beceripuani -= 1
                    elif tercih == 5:
                        oyuncu1.toplayicilik += 1
                        print("Toplayıcılığınız 1 Puan Arttırıldı")
                        beceripuani -= 1
                else:
                    print("Geçersiz Tercih Yaptınız Lütfen Düzgün Sayı Giriniz")

            print("Tüm beceri puanları harcandı. Seviye atlama işlemi tamamlandı.")

            oyuncu1.tecrube -= 100
            anamenu1.print_anamenu()
        else:
            print("Yeteri kadar Tecrübeniz Bulunmamaktadır.Tecrübe Kazanın")
            anamenu1.print_anamenu()


class Ozellikgosterme:
    def __init__(self):
        pass

    def ozellikgosterme1(self):
        boslukbirakma()
        print()
        print("Paranız : " + str(oyuncu1.para))
        print()
        print("Canınız : " + str(oyuncu1.cani))
        print()
        print("Tokluk Durumunuz : " + str(oyuncu1.tokluk))
        print()
        print("Hijyeniniz : " + str(oyuncu1.hijyen))
        print()
        print("Eğlenceniz : " + str(oyuncu1.eglence))
        print()
        print("Uykusuzluğunuz :" + ' ' + str(oyuncu1.uyku))
        print()
        print("Gücünüz : " + str(oyuncu1.guc))
        print()
        print("çevikliğiniz : " + str(oyuncu1.cevik))
        print()
        print("Dayanıklılığınız : " + str(oyuncu1.dayan))
        print()
        print("Karizmanız : " + str(oyuncu1.karizma))
        print()
        print("toplayıcılığınız : " + str(oyuncu1.toplayicilik))
        print()
        print("Seviyeniz : " + str(oyuncu1.seviye))
        print()
        print("Tecrübeniz : " + str(oyuncu1.tecrube))
        print()
        anamenu1.print_anamenu()


class boslukbirakma:
    def __init__(self):
        for i in range(1, 15):
            print()


class gameover:
    def __init__(self):
        print("GAME OVER")


class oncekarakter:
    def __init__(self):
        while oyuncu1.cani > 0:
            svk = input(" İlk Saldırıyı Siz Gerçekleştiriyorusnuz.Saldırmak İçin 1'e Basın.Kaçmak İçin 2'ye Basınız")
            try:
                svk = int(svk)
            except ValueError:
                print("Geçerli Değer giriniz")
                continue

            if int(svk) == 1:
                print("İlk Saldırıyı Siz Gerçekleştiriyorsunuz")
                hasar1 = oyuncu1.guc * 4
                haydut1.cani -= hasar1 - (hasar1 * (4 * haydut1.dayan / 100) - 1)
                print("Kalan Canınız: " + str(oyuncu1.cani))
                print("Haydutun Kalan Canı: " + str(haydut1.cani))
                if haydut1.cani <= 0:
                    print("Haydutu Yendiniz Tebrikler")
                    oyuncu1.tecrube += 30
                    oyuncu1.para += 30
                    haydut1.cani = 50
                    anamenu1.print_anamenu()
                print("Şimdi Haydutun Sırası")
                ahasar = haydut1.guc * 4
                oyuncu1.cani -= ahasar - (ahasar * (4 * oyuncu1.dayan / 100) - 1)
                print("Kalan Canınız: " + str(oyuncu1.cani))
                print("Haydutun Kalan Canı: " + str(haydut1.cani))
                if oyuncu1.cani <= 0:
                    gameover()

            elif int(svk) == 2:
                kacma = random.randint(oyuncu1.cevik * 2, 100)
                if kacma > 50:
                    print("Tebrikler Başarıyla Kaçtınız.Umarım Kimse Görmemiştir")
                    anamenu1.print_anamenu()
                else:
                    print("Kaçamadınız ")
            else:
                print("Geçerli Sayı Giriniz")


class oncekarakterorta:
    def __init__(self):
        while oyuncu1.cani > 0:
            svk = input("Saldırmak İçin 1'e Basın.Kaçmak İçin 2'ye Basınız")
            try:
                svk = int(svk)
            except ValueError:
                print("Geçerli Değer giriniz")
                continue
            if int(svk) == 1:
                print("İlk Saldırıyı Siz Gerçekleştiriyorsunuz")
                hasar1 = oyuncu1.guc * 4
                haydut2.cani -= hasar1 - (hasar1 * (4 * haydut2.dayan / 100) - 1)
                print("Kalan Canınız: " + str(oyuncu1.cani))
                print("Haydutun Kalan Canı: " + str(haydut2.cani))
                if haydut2.cani <= 0:
                    print("Haydutu Yendiniz Tebrikler")
                    oyuncu1.tecrube += 60
                    oyuncu1.para += 60
                    haydut2.cani = 70
                    anamenu1.print_anamenu()
                print("Şimdi Haydutun Sırası")
                ahasar = haydut2.guc * 4
                oyuncu1.cani -= ahasar - (ahasar * (4 * oyuncu1.dayan / 100) - 1)
                print("Kalan Canınız: " + str(oyuncu1.cani))
                if oyuncu1.cani <= 0:
                    gameover()

            elif int(svk) == 2:
                kacma = random.randint(oyuncu1.cevik * 2, 100)
                if kacma > 50:
                    print("Tebrikler Başarıyla Kaçtınız.Umarım Kimse Görmemiştir")
                    anamenu1.print_anamenu()
                else:
                    print("Kaçamadınız ")
            else:
                print("Geçerli Sayı giriniz")


class oncekarakterzor:
    def __init__(self):
        while oyuncu1.cani > 0:
            svk = input("Saldırmak İçin 1'e Basın.Kaçmak İçin 2'ye Basınız")
            try:
                svk = int(svk)
            except ValueError:
                print("Geçerli Değer giriniz")
                continue
            if int(svk) == 1:
                print("İlk Saldırıyı Siz Gerçekleştiriyorsunuz")
                hasar1 = oyuncu1.guc * 4
                haydut3.cani -= hasar1 - (hasar1 * (4 * haydut3.dayan / 100) - 1)
                print("Kalan Canınız: " + str(oyuncu1.cani))
                print("Haydutun Kalan Canı: " + str(haydut3.cani))
                if haydut3.cani <= 0:
                    print("Haydutu Yendiniz Tebrikler")
                    oyuncu1.tecrube += 100
                    oyuncu1.para += 100
                    haydut3.cani = 90
                    anamenu1.print_anamenu()
                print("Şimdi Haydutun Sırası")
                ahasar = haydut3.guc * 4
                oyuncu1.cani -= ahasar - (ahasar * (4 * oyuncu1.dayan / 100) - 1)
                print("Kalan Canınız: " + str(oyuncu1.cani))
                print("Haydutun Kalan Canı: "+str(haydut3.cani))

                if oyuncu1.cani <= 0:
                    gameover()

            elif int(svk) == 2:
                kacma = random.randint(oyuncu1.cevik * 2, 100)
                if kacma > 50:
                    print("Tebrikler Başarıyla Kaçtınız.Umarım Kimse Görmemiştir")
                    anamenu1.print_anamenu()
                else:
                    print("Kaçamadınız ")
            else:
                print("Geçerli Sayı giriniz")


class oncehaydut:
    def __init__(self):
        while oyuncu1.cani > 0:

            print("İlk Saldırıyı Haydut Gerçekleştiriyor")
            ahasar = haydut1.guc * 4
            oyuncu1.cani -= ahasar - (ahasar * (4 * oyuncu1.dayan / 100) - 1)
            print("Kalan Canınız: " + str(oyuncu1.cani))
            print("Haydutun Kalan Canı: " + str(haydut1.cani))
            if oyuncu1.cani <= 0:
                gameover()
            svk1 = input("Saldırmak İçin 1'e Basınız.Kaçmak İçin 2'ye Basınız")

            try:
                svk1 = int(svk1)
            except ValueError:
                print("Geçerli Değer giriniz")
                oyuncu1.cani += ahasar - (ahasar * (4 * oyuncu1.dayan / 100) - 1)
                continue

            if int(svk1) == 1:
                print("Saldırı Gerçekleştiriyorsunuz")
                hasar1 = oyuncu1.guc * 4
                haydut1.cani -= hasar1 - (hasar1 * (4 * haydut1.dayan / 100) - 1)
                print("Kalan canınız: " + str(oyuncu1.cani))
                print("Haydutun Kalan Canı: " + str(haydut1.cani))
                if haydut1.cani <= 0:
                    print("Haydutu Yendiniz Tebrikler")
                    oyuncu1.tecrube += 30
                    oyuncu1.para += 30
                    haydut1.cani = 50
                    anamenu1.print_anamenu()

            elif int(svk1) == 2:
                kacma = random.randint(oyuncu1.cevik * 2, 100)
                if kacma > 50:
                    print("Tebrikler Başarıyla Kaçtınız.Umarım Kimse Görmemiştir")
                    anamenu1.print_anamenu()
                else:
                    print("Kaçamadınız ")
            else:
                print("Geçerli Sayı giriniz")


class oncehaydutorta:
    def __init__(self):
        while oyuncu1.cani > 0:

            print("İlk Saldırıyı Haydut Gerçekleştiriyor")
            ahasar = haydut2.guc * 4
            oyuncu1.cani -= ahasar - (ahasar * (4 * oyuncu1.dayan / 100) - 1)
            print("Kalan Canınız: " + str(oyuncu1.cani))
            print("Haydutun Kalan Canı: " + str(haydut2.cani))
            if oyuncu1.cani <= 0:
                gameover()
            svk1 = input("Saldırmak İçin 1'e Basınız.Kaçmak İçin 2'ye Basınız")
            try:
                svk1 = int(svk1)
            except ValueError:
                print("Geçerli Değer giriniz")
                oyuncu1.cani += ahasar - (ahasar * (4 * oyuncu1.dayan / 100) - 1)
                continue
            if int(svk1) == 1:
                print("Saldırı Gerçekleştiriyorsunuz")
                hasar1 = oyuncu1.guc * 4
                haydut2.cani -= hasar1 - (hasar1 * (4 * haydut2.dayan / 100) - 1)
                print("Kalan canınız: " + str(oyuncu1.cani))
                print("Haydutun Kalan Canı: " + str(haydut2.cani))
                if haydut2.cani <= 0:
                    print("Haydutu Yendiniz Tebrikler")
                    oyuncu1.tecrube += 60
                    oyuncu1.para += 60
                    haydut2.cani = 70
                    anamenu1.print_anamenu()

            elif int(svk1) == 2:
                kacma = random.randint(oyuncu1.cevik * 2, 100)
                if kacma > 50:
                    print("Tebrikler Başarıyla Kaçtınız.Umarım Kimse Görmemiştir")
                    anamenu1.print_anamenu()
                else:
                    print("Kaçamadınız ")
            else:
                print("Geçerli Sayı giriniz")


class oncehaydutzor:
    def __init__(self):
        while oyuncu1.cani > 0:

            print("İlk Saldırıyı Haydut Gerçekleştiriyor")
            ahasar = haydut3.guc * 4
            oyuncu1.cani -= ahasar - (ahasar * (4 * oyuncu1.dayan / 100) - 1)
            print("Kalan Canınız: " + str(oyuncu1.cani))
            print("Haydutun Kalan Canı: " + str(haydut3.cani))
            if oyuncu1.cani <= 0:
                gameover()
            svk1 = input("Saldırmak İçin 1'e Basınız.Kaçmak İçin 2'ye Basınız")
            try:
                svk1 = int(svk1)
            except ValueError:
                print("Geçerli Değer giriniz")
                oyuncu1.cani += ahasar - (ahasar * (4 * oyuncu1.dayan / 100) - 1)
                continue

            if int(svk1) == 1:
                print("Saldırı Gerçekleştiriyorsunuz")
                hasar1 = oyuncu1.guc * 4
                haydut3.cani -= hasar1 - (hasar1 * (4 * haydut3.dayan / 100) - 1)
                print("Kalan canınız: " + str(oyuncu1.cani))
                print("Haydutun Kalan Canı: " + str(haydut3.cani))
                if haydut3.cani <= 0:
                    print("Haydutu Yendiniz Tebrikler")
                    oyuncu1.tecrube += 100
                    oyuncu1.para += 100
                    haydut3.cani = 90
                    anamenu1.print_anamenu()

            elif int(svk1) == 2:
                kacma = random.randint(oyuncu1.cevik * 2, 100)
                if kacma > 50:
                    print("Tebrikler Başarıyla Kaçtınız.Umarım Kimse Görmemiştir")
                    anamenu1.print_anamenu()
                else:
                    print("Kaçamadınız ")
            else:
                print("Geçerli Sayı giriniz")


anamenu1 = Anamenu()
kampalani1 = Kampalani()
sifahane1 = Sifahane()
han1 = Han()
macera1 = Macera()
seviyeatla1 = Seviyeatla()
ozellikgoster1 = Ozellikgosterme()

anamenu1.print_anamenu()