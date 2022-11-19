#eren mutlu C grubu yazem odev 22010104013 19/11/2022

import os


contemizle = lambda:os.system('cls')


class gereklilikler:
    bolumu = 1
    deneyimenaz = 3
    deneyimencok = 7
    ingseviyeazami = 2


class kisi:
    yazibolum = ""
    yaziingseviye = ""
    bolumu = 0
    denemeyimi = 0
    ingseviye = 0
    sonucu = 0

def main():
    secim = 0
    contemizle()
    print("hosgelniz oncelikle bolumunuzu ogrenebilirbirmiyiz")
    print("1= Matematik")
    print("2= Bilgisayar Muh.")
    print("3= elektrik-elektronik Muh.")
    print("4= Mekatronik Muh.")
    print("5= Hicbiri")
    secim = int(input("seciminiz = "))
    if secim >=6:
        print("gecersiz secim")
        return main()
    if secim ==1:
        kisi.yazibolum = "Matematik"
        kisi.bolumu = 1
        return ikiasama()
    if secim ==2:
        kisi.yazibolum = "elektrik-elektronik Muh."
        kisi.bolumu = 1
        return ikiasama()
    if secim ==3:
        kisi.yazibolum = "Bilgisayar Muh."
        kisi.bolumu = 1
        return ikiasama()
    if secim ==4:
        kisi.yazibolum = "Memaktronik Muh."
        kisi.bolumu = 1
        return ikiasama()
    if secim ==5:
        kisi.yazibolum = "gecersiz bolum"
        return ikiasama()

def ikiasama():
    contemizle()
    secim = 0
    print("ingilizce seviyeniz")
    print("1= harika")
    print("2= iyi")
    print("3= kotu")
    secim = int(input("seciminiz = "))

    if secim >=4:
        print("gecersiz sencenek")
        return ikiasama()

    if secim == 1:
        kisi.ingseviye = 3
        kisi.yaziingseviye = "harika"
        return ucasama()
    if secim == 2:
        kisi.ingseviye = 2
        kisi.yaziingseviye = "iyi"
        return ucasama()
    if secim == 3:
        kisi.yaziingseviye = "kotu"
        kisi.ingseviye = 1
        return ucasama()


def ucasama():
    tecrube = 0
    print("daha once bu konularda deneyimniz oldugumu olduysa kac yil")
    print("yapay zeka")
    print("makine ogrenmesi")
    print("bilgisayar muhendisligi")
    tecrube = int(input("tecrube sureniz = "))
    kisi.denemeyimi = tecrube
    return sonasama()
        

def sonasama():
    contemizle()
    print("bolumunuz",kisi.yazibolum)
    print("ing seviyeniz",kisi.yaziingseviye)
    print("deneyiminiz",kisi.denemeyimi,"yil")
    if kisi.bolumu == 1:
        if kisi.ingseviye >=2:
            if kisi.denemeyimi >=3:
                kisi.sonucu = 1
            else:
                kisi.sonucu = 0
        else:
            kisi.sonucu = 0
    else:
        kisi.sonucu = 0
    return final()


def final():
    if kisi.sonucu == 1:
        print("alindiniz")   
    else:
        print("alinamadiniz")

    


main()
    




