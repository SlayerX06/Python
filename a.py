num1 = int(input("1. sayıyı giriniz"))
num2 = int(input("2. sayıyı giriniz"))

islem = input("İşlem seçiniz. +:Toplama, -:Çıkarma, x:Çarpma, /:Bölme")

if islem == "+":
    print(num1+num2)
elif islem == "-":
    print(num1-num2)
elif islem == "x":
    print(num1*num2)
elif islem == "/":
    print(num1/num2)