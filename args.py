# *arglar = tüm argümanları tek bir tuple değişkeninde saklamak için kullanılır.
# args, fonksiyona geçirilen tüm argümanları bir tuple olarak saklar

def add(*args): # başa koyulan yıldız işareti, args'ın bir tuple olduğunu belirtir. böylece fonksiyona istediğimiz kadar argüman geçirebiliriz.
    total = 0
    args = list(args)  # args'ı listeye çeviriyoruz. çünkü normalde tuple'dır ve değiştirilemez.
    args[0] = 10  # şimdi args'ın ilk elemanını değiştirebiliriz.
    for num in args:
        total += num
    return total

print(add(1, 2, 3, 4, 5))  