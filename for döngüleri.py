#while döngüsü sürekli olarak belirli bir koşul doğru olduğu sürece çalışır.
#for döngüsü ise belirli bir süre çalışır.

#for i in range(10):  # 0'dan başlayarak 10'a kadar olan sayılar için döngü
#    print(i+1)  # i'yi 1 artırarak yazdırır (1'den 10'a kadar)

#for i in range(50, 100+1, 2):  # 50'den başlayarak 100'e kadar olan sayılar için döngü
#    print(i)  # i'yi yazdırır (50, 52, 54, ..., 100) bu sıra ikişer ikişer artar

#for i in "Python":  # "Python" kelimesindeki her karakter için döngü
#    print(i)  # Her karakteri tek tek yazdırır (P, y, t, h, o, n)

import time

for i in range(10, 0, -1):  # 10'dan başlayarak 1'e kadar olan sayılar için döngü
    print(i)  # i'yi yazdırır (10, 9, 8, ..., 1)
    time.sleep(1)  # Her sayıyı yazdırdıktan sonra 1 saniye bekler
print("Mutlu Yıllar!")  # Döngü tamamlandıktan sonra "Mutlu Yıllar!" yazdırır