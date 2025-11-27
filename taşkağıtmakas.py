import random

while True:
    hamleler = ['taş', 'kağıt', 'makas']

    bilgisayar = random.choice(hamleler)
    oyuncu = None

    while oyuncu not in hamleler:
        oyuncu = input("Taş, Kağıt veya Makas seçiniz: ").lower()

    if bilgisayar == oyuncu:
        print("Bilgisayar: ", bilgisayar)
        print("Oyuncu: ", oyuncu)
        print("Sonuç: Berabere!")
    elif oyuncu == 'taş':
        if bilgisayar == 'kağıt':
            print("Bilgisayar: ", bilgisayar)
            print("Oyuncu: ", oyuncu)
        print("Sonuç: Bilgisayar kazandı!")
    elif bilgisayar == 'makas':
        print("Bilgisayar: ", bilgisayar)
        print("Oyuncu: ", oyuncu)
        print("Sonuç: Oyuncu kazandı!")
    elif oyuncu == 'makas':
        if bilgisayar == 'taş':
            print("Bilgisayar: ", bilgisayar)
            print("Oyuncu: ", oyuncu)
            print("Sonuç: Bilgisayar kazandı!")
    elif bilgisayar == 'kağıt':
        print("Bilgisayar: ", bilgisayar)
        print("Oyuncu: ", oyuncu)
        print("Sonuç: Oyuncu kazandı!")
    elif oyuncu == 'kağıt':
        if bilgisayar == 'makas':
            print("Bilgisayar: ", bilgisayar)
            print("Oyuncu: ", oyuncu)
            print("Sonuç: Bilgisayar kazandı!")
    elif bilgisayar == 'taş':
        print("Bilgisayar: ", bilgisayar)
        print("Oyuncu: ", oyuncu)
        print("Sonuç: Oyuncu kazandı!")

        
    tekrar = input("Tekrar oynamak ister misiniz? (e/h): ").lower()
    if tekrar != 'e':
        break
print("Oyun bitti. Teşekkürler!")
    