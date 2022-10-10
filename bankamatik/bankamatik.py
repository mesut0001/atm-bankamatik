kart_sifre = 1234
bakiye = 1000
sifre_sayac = 3
login = False

while True:
    if login == False:
        sifre = int(input("Hoşgeldiniz! Lütfen şifrenizi giriniz"))
    if sifre == kart_sifre:
          login = True
          print("""
1.Para çekme
2.Para yatırma
3.Bakiye sorgulama
4.Kart iade
          """)
          secim = int(input("Hangi işlemi yapmak istiyorsunuz?"))
          if secim == 1:
              miktar = int(input("Kaç TL çekmek istiyorsunuz?"))
              if bakiye < miktar:
                  print("Yeterli bakiyeniz bulunmamaktadır")
                  continue
              bakiye -= miktar
          elif  secim == 2:
              miktar = int(input("Kaç TL yatırmak istiyorsunuz?"))
              bakiye += miktar
          elif  secim == 3:
              print("Bakiyeniz {} TL".format(bakiye))
          elif  secim == 4:
              print("Yine bekleriz")
              break
          else:
              print("Lütfen 1-4 arasında bir rakam giriniz")
    else:
        sifre_sayac -= 1
        if  sifre_sayac <= 0:
            print("Kartınız bloke olmuştur. Lütfen banka ile irtibata geçiniz.")
            break








