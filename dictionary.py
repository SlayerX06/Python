#dictionary = anahtar-değer çiftlerini saklamak için kullanılan bir veri yapısıdır
#sözlükler süslü parantez {} içinde tanımlanır ve elemanlar virgül ile ayrılır
#sözlüklerin elemanlarına erişim, anahtar (key) ile yapılır

başkentler = {"Türkiye": "Ankara",
              "Almanya": "Berlin",
              "Fransa": "Paris",
              "İtalya": "Roma",}
başkentler.update({"İspanya": "Madrid"}) # sözlüğe yeni bir anahtar-değer çifti ekler
başkentler.update({"Türkiye": "İstanbul"}) # sözlükteki bir anahtarın değerini değiştirir
başkentler.pop("Fransa") # sözlükten bir anahtar-değer çiftini çıkarır
başkentler.clear() # sözlüğün tüm elemanlarını çıkarır


#print(başkentler["Türkiye"]) # anahtara göre değeri yazdırır
#print(başkentler.get("İspanya")) # anahtara göre değeri yazdırır ilk örnekte anahtar yoksa hata verir, get() metodu None döner
#print(başkentler.keys()) # sözlüğün tüm anahtarlarını yazdırır
#print(başkentler.values()) # sözlüğün tüm değerlerini yazdırır
#print(başkentler.items()) # sözlüğün tüm anahtar-değer çiftlerini yazdırır
for ülke, başkent in başkentler.items(): # sözlükteki her anahtar-değer çifti için döngü
   print(f"{ülke} - {başkent}") # anahtar ve değeri yazdırır

