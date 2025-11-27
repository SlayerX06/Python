# İç içe fonksiyon çağrıları, bir fonksiyonun içinde başka bir fonksiyon çağrısı yapmayı sağlar.
# İlk önce iç fonksiyon çalıştırılır ve ardından dış fonksiyon çalıştırılır.
# İç fonksiyonda döndürülen değerler, dış fonksiyona argüman olarak geçilir.

#num = input("Bir sayı giriniz: ")
#num = float(num)
#num = abs(num)  # abs() fonksiyonu, bir sayının mutlak değerini döndürür.
#num = round(num)  # round() fonksiyonu, bir sayıyı en yakın tam sayıya yuvarlar.

print(round(abs(float(input("Bir sayı giriniz: ")))))  # İç içe fonksiyon çağrısı örneği