# Anahtar kelime argümanları, bir fonksiyona argümanları isimleriyle birlikte geçirmeyi sağlar.
#  Bu, özellikle bir fonksiyonun birçok parametresi olduğunda veya bazı argümanları atlamak istediğinizde faydalıdır.
# Bu argümanlar, fonksiyon çağrısında belirtilen isimlere göre eşleştirilir.

def hello(first, middle, last):
    print("Merhaba! " + first + " " + middle + " " + last)

hello(last="Düşürge", first="İbrahim", middle="Kaan")  # Anahtar kelime argümanları kullanılarak çağrılır
