import random

x = random.randint(1,6) #randint komutu seçilen aralıkta rastgele bir tam sayı üretir.
y = random.random() #random komutu 0 ile 1 arasında rastgele bir ondalık sayı üretir.

myList = ["Taş","Kağıt","Makas"]
z = random.choice(myList) #choice komutu verilen listeden rastgele bir eleman seçer.

cards = ["As","2","3","4","5","6","7","8","9","10","J","Q","K"]
random.shuffle(cards) #shuffle komutu verilen listedeki elemanların sırasını rastgele karıştırır.

print(cards)
