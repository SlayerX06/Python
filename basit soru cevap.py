def yeni_oyun():
    tahminler = []
    dogrusayisi = 0
    soru_sayısı = 1

    for key in sorular:
        print("-------------------------")
        print(key)
        for i in cevaplar[soru_sayısı - 1]:
            print(i)
        soru_sayısı += 1
        tahmin = input("Cevabınızı giriniz (A, B, C, D): ").upper()
        tahminler.append(tahmin)
        dogrusayisi += cevap_kontrol(sorular.get(key), tahmin)

    skor_goster(dogrusayisi, tahminler)

def cevap_kontrol(dogru_cevap, kullanici_cevabi):
    if dogru_cevap == kullanici_cevabi:
        print("Doğru!")
        return 1
    else:
        print("Yanlış!")
        return 0

def skor_goster(dogrusayisi, tahminler):
    print("-------------------------")
    print("Sonuçlar")
    print("-------------------------")
    print("Cevaplar: ", end="")
    for i in sorular:
        print(sorular.get(i), end=" ")
    print()
    print("Tahminler: ", end="")
    for i in tahminler:
        print(i, end=" ")
    print()

    skor = int((dogrusayisi / len(sorular)) * 100)
    print("Skorunuz: " + str(skor) + " puan")

    tekrar_oyna()

def tekrar_oyna():
    tekrar = input("Tekrar oynamak ister misiniz? (e/h): ").lower()
    if tekrar == 'e':
        yeni_oyun()
    else:
        print("Oyun bitti. Teşekkürler!")

sorular = {
    "Türkiye'nin başkenti neresidir?": "A",
    "Dünya düz müdür?": "D",
    "Dünya'nın en yüksek dağı hangisidir?": "C",
    "Türkiye'nin ilk cumhurbaşkanı kimdir?": "B",
    "İstanbul'un fethi hangi yılda gerçekleşti?": "A"
}

cevaplar = [["A) Ankara", "B) İstanbul", "C) İzmir", "D) Antalya"],
              ["A) Evet", "B) Bazen", "C) Hayır", "D) Ben Marslıyım" ],
              ["A) K2", "B) Kangchenjunga", "C) Everest", "D) Lhotse"],
              ["A) İsmet İnönü", "B) Mustafa Kemal Atatürk", "C) Turgut Özal", "D) Süleyman Demirel"],
              ["A) 1453", "B) 1492", "C) 1326", "D) 1517"]]

yeni_oyun()