# exceptions = bir hata oluştuğunda programın normal akışını kesintiye uğratan olaylardır.

try:
    num1 = int(input("Bir sayı girin: "))
    num2 = int(input("Bir sayı girin: "))
    result = num1 / num2

except ZeroDivisionError: # bu kodların sonuna "as e" eklenirse hatanın detaylarını görebiliriz.
    print("Hata: Bir sayı sıfıra bölünemez. APTALSIN!")
except ValueError:
    print("Sadece sayı gir kardeşim uğraştırma bizi")
except Exception:
    print("Bilinmeyen bir sebepten dolayı bir hata oluştu.")
else:
    print("Sonuç:", result)

finally: # finally bloğu hata olsa da olmasa da her durumda çalışır.
    print("Program sonlandı.")