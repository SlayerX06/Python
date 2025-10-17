#index [] = İndex bize bir dizinin (list, tuple, string vb.) belirli bir öğesinin konumunu (indeksini) bulmamıza yarar.
#İndeksler 0'dan başlar, yani ilk öğe 0. indekstir.
#Negatif indeksler ise dizinin sonundan başlayarak sayar, yani -1 son öğeyi temsil eder.

name = "ibrahim Düşürge"

#if (name[0].islower()):
 #   name = name.capitalize()  # İlk harfi büyük yapar

firs_name = name[0:7].upper()  # İlk 7 karakteri alır ve büyük harfe çevirir
last_name = name[8:].lower()  # 8. indeksten sonuna kadar alır ve küçük harfe çevirir
last_character = name[-1]  # Son karakteri alır

print(firs_name)  # İndeks kullanarak karaktere erişim
print(last_name)  # Dilimleme kullanarak alt dizeye erişim
print(last_character)  # Negatif indeks kullanarak son karaktere erişim