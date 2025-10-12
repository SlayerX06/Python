import random

sayi1 = random.randint(1,100)

sayi2 = int(input("Sayı giriniz"))

while sayi1 != sayi2:
    if sayi1 > sayi2: print("Sayınız daha büyük olmalı")
    elif sayi1 < sayi2: print("Sayınız daha küçük olmalı")

    sayi2 = int(input("Yeni sayı giriniz"))

if sayi1 == sayi2: print("DOĞRU BİLDİNİZ!")