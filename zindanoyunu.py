import random

oyuncu = input("Merhaba oyuncu sınıfını seç: A:Şövalye, B:Okçu, C:Büyücü ")

if oyuncu == "A":
    Can = 150
    Hasar = random.randint(20,30)
    Karizma = random.randint(1,10)
elif oyuncu == "B":
    Can = 100
    Hasar = random.randint(30,50)
    Karizma = random.randint(1,10)
elif oyuncu == "C":
    Can = 75
    Hasar = random.randint(40,60)
    Karizma = random.randint(1,10)
    Mana = 100

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

print("Karşına bir " + enemyname + " çıktı! Ne yapacaksın? ")
eylem = input("A:Saldır, B:Savun, C:Konuş, D:Yetenek, E:Pes Et ")

while enemy["Can"] > 0 and Can > 0:
    if eylem == "A":
        enemy["Can"] -= Hasar
        print("Düşmana " + str(Hasar) + " hasar verdin. Düşmanın kalan canı: " + str(enemy["Can"]))
        if enemy["Can"] > 0 and Can > 0:
            eylem = input("Şimdi ne yapacaksın? ")
    elif eylem == "B":
        print("Savunma durumuna geçtin bu tur hasar almayacaksın.")
        if enemy["Can"] > 0 and Can > 0:
            eylem = input("Şimdi ne yapacaksın? ")
    elif eylem == "C":
        if Karizma > enemy["Karizma"]:
            print("Düşman seninle dost oldu!")
            break
        else:
            print("Düşman seni dinlemedi.")
            if enemy["Can"] > 0 and Can > 0:
               eylem = input("Şimdi ne yapacaksın? ")
    elif eylem == "D" and oyuncu == "C":
        if Mana >= 20:
            enemy["Can"] -= Hasar * 2
            Mana -= 20
            print("Büyü yaptın! Düşmana " + str(Hasar * 2) + " hasar verdin. Düşmanın kalan canı: " + str(enemy["Can"]))
            if enemy["Can"] > 0 and Can > 0:
               eylem = input("Şimdi ne yapacaksın? ")
        else:
            print("Yeterli manan yok!")
            if enemy["Can"] > 0 and Can > 0:
               eylem = input("Şimdi ne yapacaksın? ")
    elif eylem == "E":
        print("Pes ettin. Oyun bitti.")
        break

    if enemy["Can"] > 0 and eylem != "B":
        Can -= enemy["Hasar"]
        print("Düşman sana " + str(enemy["Hasar"]) + " hasar verdi. Kalan canın: " + str(Can))
    elif enemy["Can"] > 0 and eylem == "B":
        print("Düşmanın vuruşunu engelledin!")

    if Can <= 0:
        print("Oyuncu öldü. Oyun bitti.")

    if enemy["Can"] <= 0:
        print("Düşman öldü. Tebrikler!")
        break