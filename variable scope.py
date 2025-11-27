# Değişkenlerin kapsamı (scope), bir değişkenin erişilebilir olduğu alanı tanımlar.
# Bir değişkenin kapsamı, genellikle tanımlandığı yere bağlıdır.
# Global değişkenler, tüm programda erişilebilirken, yerel değişkenler sadece tanımlandıkları fonksiyon içinde erişilebilir.
# Bir değişkenin hem global hem de yerel değeri olabilir, bu durumda yerel değişken global değişkeni geçersiz kılar. 

ad = "İbrahim"  # Global değişkendir. Kodun her yerinden erişilebilir.

def selamla():
    ad = "Ahmet"  # Yerel değişkendir. Sadece bu fonksiyon içinde erişilebilir.
    print("Merhaba " + ad)

print(ad)  # Global değişkene erişilebilir.
selamla()  # Bu değer öncelikle fonksiyonun içindeki yerel değeri alır.
