import random

oyuncu = input("""Merhaba oyuncu sınıfını seç:
               A:Şövalye (Yüksek can, düşük hasar ve savunma yeteneği)
               B:OKçu (Ortalama can, ortalama hasar, kafadan vuruş özelliği ile tek atma şansı)
               C:Büyücü (Düşük can, yüksek hasar, büyü yeteneği, can yenileme) """)

if oyuncu == "A":
    Can = 150
    Hasar = random.randint(20,30)
    Karizma = random.randint(1,10)
    print("Şövalye seçtin! Canın: " + str(Can) + ", Hasarın: " + str(Hasar) + ", Karizman: " + str(Karizma))
elif oyuncu == "B":
    Can = 100
    Hasar = random.randint(30,50)
    Karizma = random.randint(1,10)
    print("Okçu seçtin! Canın: " + str(Can) + ", Hasarın: " + str(Hasar) + ", Karizman: " + str(Karizma))
elif oyuncu == "C":
    Can = 75
    Hasar = random.randint(40,60)
    Karizma = random.randint(1,10)
    Mana = 100
    print("Büyücü seçtin! Canın: " + str(Can) + ", Hasarın: " + str(Hasar) + ", Karizman: " + str(Karizma) + ", Manan: " + str(Mana))


Goblin = {"Can": 30, "Hasar": random.randint(5,10), "Karizma": random.randint(1,2)}
Ork = {"Can": 50, "Hasar": random.randint(20,25), "Karizma": random.randint(1,5)}
Troll = {"Can": 100, "Hasar": random.randint(20,40), "Karizma": random.randint(1,10)}
Ejderha = {"Can": 200, "Hasar": random.randint(40,60), "Karizma": random.randint(5,10)}

enemies = [Goblin,Ork,Troll,Ejderha]
enemy = random.choice(enemies)

if enemy == Goblin:
    enemyname = "Goblin"
elif enemy == Ork:
    enemyname = "Ork"
elif enemy == Troll:
    enemyname = "Troll"
elif enemy == Ejderha:
    enemyname = "Ejderha"

enemymoves = random.randint(1,3)

print("Karşına bir " + enemyname + " çıktı! Ne yapacaksın? ")

if oyuncu == "A":
    eylem = input("A:Saldır, B:Savun, C:Gözlemle D:Konuş, E:Pes et")
elif oyuncu == "B":
    eylem = input("A:Saldır, B:Kafadan vuruş, C:Gözlemle D:Konuş, E:Pes et")
elif oyuncu == "C":
    eylem = input("A:Saldır, B:Büyü yap, C:Gözlemle D:Konuş, E:Pes et, F:İyileşme")

while enemy["Can"] > 0 and Can > 0:
    if enemymoves == 1:
        Can -= enemy["Hasar"]
        print("Düşman sana " + str(enemy["Hasar"]) + " hasar verdi. Kalan canın: " + str(Can))
        enemymoves = random.randint(1,3)
    elif enemymoves == 2:
        print("Düşman savunma durumuna geçti ve bu tur hasar vermedi.")
        enemymoves = random.randint(1,3)
    elif enemymoves == 3:
        print("Düşman sana saldırmak yerine seni gözlemliyor.")
        enemymoves = random.randint(1,3)
    if eylem == "A":
        enemy["Can"] -= Hasar
        print("Düşmana " + str(Hasar) + " hasar verdin. Düşmanın kalan canı: " + str(enemy["Can"]))
        if enemy["Can"] > 0 and Can > 0:
            eylem = input("Şimdi ne yapacaksın? ")
    elif eylem == "B" and oyuncu == "A":
        print("Savunma durumuna geçtin bu tur hasar almayacaksın.")
        if enemy["Can"] > 0 and Can > 0:
            eylem = input("Şimdi ne yapacaksın? ")
    elif eylem == "B" and oyuncu == "B":
        şans = random.randint(1,4)
        if şans == 4:
            enemy["Can"] = 0
            print("isabetli bir atış yaptın ve düşmanını yendin!")
        elif şans != 4:
            print("İsabet ettiremedin. Düşman hasar almadı :(")
            eylem = input("Şimdi ne yapacaksın?")
    elif eylem == "B" and oyuncu == "C":
        if Mana >= 20:
            enemy["Can"] -= Hasar * 2
            Mana -= 20
            print("Büyü yaptın! Düşmana " + str(Hasar * 2) + " hasar verdin. Düşmanın kalan canı: " + str(enemy["Can"]))
            if enemy["Can"] > 0 and Can > 0:
               eylem = input("Şimdi ne yapacaksın? ")
        else: 
            print("Yeterli manan yok!")
            eylem = input("Şimdi ne yapacaksın? ")
    elif eylem == "D":
        if Karizma > enemy["Karizma"]:
            print("Düşman seninle dost oldu!")
            break
        else:
            print("Düşman seni dinlemedi.")
            if enemy["Can"] > 0 and Can > 0:
               eylem = input("Şimdi ne yapacaksın? ")
    elif eylem == "C":
        print("Düşmanın canı: " + str(enemy["Can"]) + ", hasarı: " + str(enemy["Hasar"]) + ", karizması: " + str(enemy["Karizma"]))
        eylem = input("Şimdi ne yapacaksın? ")
    elif eylem == "F" and oyuncu == "C":
        if Mana >= 20:
            Can += 30
            Mana -= 20
            print("İyileştin! Kalan canın: " + str(Can))
            if enemy["Can"] > 0 and Can > 0:
               eylem = input("Şimdi ne yapacaksın? ")
        else:
            print("Yeterli manan yok!")
            if enemy["Can"] > 0 and Can > 0:
               eylem = input("Şimdi ne yapacaksın? ")
    elif eylem == "E":
        print("Pes ettin. Oyun bitti.")
        break


    if Can <= 0:
        print("Oyuncu öldü. Oyun bitti.")

    if enemy["Can"] <= 0:
        print("Düşman öldü. Tebrikler!")
        break