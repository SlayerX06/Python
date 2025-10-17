islem = input("İşlem seçiniz. (+:Toplama, -:Çıkarma, x:Çarpma, /:Bölme, Bitir:Kapat) ")

num1 = int(input("1. sayıyı giriniz "))
num2 = int(input("2. sayıyı giriniz "))


while islem != "Bitir":
    if islem == "+":
       print(num1+num2)
       islem = input("İşlem seçiniz. (+:Toplama, -:Çıkarma, x:Çarpma, /:Bölme, Bitir:Kapat) ")
       num1 = int(input("1. sayıyı giriniz"))
       num2 = int(input("2. sayıyı giriniz "))
    elif islem == "-":
        print(num1-num2)
        islem = input("İşlem seçiniz. (+:Toplama, -:Çıkarma, x:Çarpma, /:Bölme, Bitir:Kapat) ")
        num1 = int(input("1. sayıyı giriniz"))
        num2 = int(input("2. sayıyı giriniz "))
    elif islem == "x":
         print(num1*num2)
         islem = input("İşlem seçiniz. (+:Toplama, -:Çıkarma, x:Çarpma, /:Bölme, Bitir:Kapat) ")
         num1 = int(input("1. sayıyı giriniz"))
         num2 = int(input("2. sayıyı giriniz "))
    elif islem == "/":
         if num2 == 0: print("Geçersiz işlem")
         islem = input("İşlem seçiniz. (+:Toplama, -:Çıkarma, x:Çarpma, /:Bölme, Bitir:Kapat) ")
         num1 = int(input("1. sayıyı giriniz"))
         num2 = int(input("2. sayıyı giriniz "))    
         if num2 != 0: print(num1/num2)
         islem = input("İşlem seçiniz. (+:Toplama, -:Çıkarma, x:Çarpma, /:Bölme, Bitir:Kapat) ")
         num1 = int(input("1. sayıyı giriniz"))
         num2 = int(input("2. sayıyı giriniz "))
    else: print("İşlem geçersiz")   

print("Hesap makinesi kapatıldı.")
print("Güle güle")   


