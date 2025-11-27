
try:
     with open("test.txt") as file:
          print(file.read()) #dosya içeriğini okur ve ekrana yazdırır
    #bu şekilde dosyanın okunması için dosya varsayılan sistem klasörü içinde olmalıdır
    #eğer farklı bir klasörde ise dosya yolunu belirtmemiz gerekir
    #örneğin: with open("C:/Users/KullaniciAdi/Desktop/test.txt") as file:
except FileNotFoundError:
     print("Dosya bulunamadı. Lütfen dosya yolunu kontrol edin.")   
