#çoklu inherit durumunda bir alt class başka bir alt classa sahip olur

class Oragnizma:

    yaşam = True

class Hayvan(Oragnizma):

    def yemek(self):
        print("Bu hayvan bir şeyler yiyor")

class Kedi(Hayvan):  #bu tanımladığımız kedi hem hayvan hem de organizma sınıfına dahildir. ikisinin de özelliklerini taşır

    def miyav(self):
        print("Kedi miyavladı")

kedi = Kedi()

print(kedi.yaşam)
kedi.yemek()
kedi.miyav()