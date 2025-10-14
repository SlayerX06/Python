#nested loops = bir döngünün içinde başka bir döngü olması durumu
#               içte döngü her tamamlandığında dıştaki döngü bir kez ilerler

satırlar = int(input("Satır sayısını giriniz: "))
sütunlar = int(input("Sütun sayısını giriniz: "))
sembol = input("Kullanılacak sembolü giriniz: ")

for i in range(satırlar): #dıştaki döngü
    for j in range(sütunlar): #içteki döngü
        print(sembol, end=" ")
    print()
#end=" " komutu printin sonuna boşluk ekler ve alt satıra geçmesini engeller    