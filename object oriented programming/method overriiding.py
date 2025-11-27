class Hayvan:
    def yemek(self):
        print("Bu hayvan bir şeyler yiyor")

class Tavşan(Hayvan):
    def yemek(self):
        print("Bu tavşan havuç yiyor")
        #burada tavşan sınıfının altına bu kodu yazarak override yaparız. kod çalışırken kendisine daha yakın olan işlevi kullanır

tavşan = Tavşan()
tavşan.yemek()