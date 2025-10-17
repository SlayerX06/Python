sayı = int(input("Sayı giriniz : "))

toplam = 0
i = 1

while i <= sayı:
    toplam = i**2 + toplam
    i = i + 1
    
print(toplam)
