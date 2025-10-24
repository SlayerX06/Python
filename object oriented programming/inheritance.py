class Hayvanlar:

    yaşam = True

    def yemek(self):
        print("Bu hayvan bir şeyler yiyor")
    
    def uyu(self):
        print("Bu hayvan uyuyor")

class Tavşan(Hayvanlar): #bu şekilde yazarak tavşanı hayvanlassının alt üyesi olarak atıyoruz.
    def koş(self):
        print("Tavşan koşuyor")

class Balık(Hayvanlar):
    def yüz(self):
        print("Balık yüzüyor")

class Kartal(Hayvanlar):
    def uç(self):
        print("Kartal uçuyor")

tavşan = Tavşan() #bu değerler hem kendi class komutlarını hem de bağlı oldukları hayvanların komutlarını uygulayabilir
balık = Balık()
kartal = Kartal()

#print(tavşan.yaşam) 
#balık.yemek()
#kartal.uyu()

tavşan.koş()
balık.yüz()
kartal.uç()

#inherit metodu aile çocuk gibidir. çocuğun ailenin özelliklerini taşıdığı gibi classlar da dahilinde olduğu üst classların kodlarına sahiptir