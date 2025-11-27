# str.format() yöntemi, bir string içinde yer tutucuları doldurmak için kullanılır.
# output gösteriminde daha fazla kontrol sağlar.

name = "Ali"
item = "kitap"

#print(name + " bir " + item + " aldı.")  # Basit string birleştirme

#print("{} bir {} aldı.".format(name, item))  # Yer tutucularla format kullanımı.
#print("{1} bir {0} aldı.".format(item, name))  # İndeks kullanarak yer tutucuları değiştirme.
#print("{name} bir {item} aldı.".format(name="Ali", item="kitap"))  # Anahtar kelimelerle yer tutucuları değiştirme.

text = "{} bir {} aldı."

print(text.format(name, item))  # Değişkenlerle format kullanımı.
print(text.format("Ayşe", "defter"))  # Farklı değerlerle format

num = 3.14159
number = 1000

print("Pi sayısı yaklaşık olarak {:.2f} olarak bilinir.".format(num))  # Ondalık basamak sayısını belirleme. 2f ondalık basamakların kaç tanesini göstericeğimizi belirler.
print("Sayı {:,} olarak gösterilir.".format(number))  # Binlik ayraç ekleme.
print("Sayı {:b} olarak gösterilir.".format(number))  # İkili (binary) gösterim.
print("Sayı {:x} olarak gösterilir.".format(number))  # Onaltılı (hexadecimal) gösterim.
print("Sayı {:o} olarak gösterilir.".format(number))  # Sekizlik (octal) gösterim.