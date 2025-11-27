#zincirleme metodlar = ard arda bir sürü metodu çağırır ve işlem yaptırırız
#                       her işlem aynı cisimde eylemi gerçeklerştirir ve sonucu iletir

class Car:
    def çalıştır(self):
        print("Arabanın motorunu çalıştırdın")
        return self
    
    def sür(self):
        print("Arabayı sürüyorsun")
        return self
    
    def fren(self):
        print("Frene bastın ve araba durdu")
        return self
    
    def söndür(self):
        print("Motoru söndürdün")
        return self  #retun ile geri dönüşü sağlarız yoksa python hata verir
    
araba = Car()

#araba.çalıştır().sür()  
#burada komuttan sonra bir nokta daha ekleyip istenen diğer komutları girebiliriz
#araba.fren().söndür()

araba.çalıştır().sür().fren().söndür()