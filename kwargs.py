#  **kwargs = tüm argümanları anahtar-değer çiftleri olarak saklamak için kullanılır.(dictionary)

def hello(**kwargs): # başa koyulan çift yıldız işareti, kwargs'ın bir dictionary olduğunu belirtir. böylece fonksiyona istediğimiz kadar anahtar-değer çifti geçirebiliriz.
    #print("Hello " + kwargs['first'] + " " + kwargs['last'])  # kwargs'dan anahtarları kullanarak değerlere erişiyoruz.
    print("Hello ", end=" ")  # end="" ile print'in sonuna yeni satır eklenmesini engelliyoruz.
    for key, value in kwargs.items():  # kwargs'ın tüm anahtar-değer çiftlerini döngü ile alıyoruz.
        print(value, end=" ")  # her değeri yazdırıyoruz.

hello(title="Kedi", first="ibrahim", last="düşürge")  # fonksiyona anahtar-değer çiftleri geçiyoruz.