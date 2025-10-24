# çoklu inheritance bazı sınıfların birden çok sınıfın alt sınıfı olma durumudur

class Av:
    def kaç(self):
        print("Bu hayvan kaçıyor")


class Avcı:
    def avlan(self):
        print("Bu hayvan avlanıyor")

class Tavşan(Av):
    pass

class Kartal(Avcı):
    pass

class Balık(Av, Avcı):  #birden çok üst sınıfa sahip değerlerde araya virgül konularak yazılır
    pass

tavşan = Tavşan()
kartal = Kartal()
balık = Balık()

tavşan.kaç()
kartal.avlan()
balık.avlan()
balık.kaç()

#birden fazla üst sınıfa sahip değerler tüm bu sınıfların kodunu kullanırken diğer değerler sadece birini kullanabilirler
