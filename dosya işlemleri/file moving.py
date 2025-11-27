import os

kaynak = "test.txt" #kaynak dosyayı belirtir
hedef = "C:\\Users\\CASPER\\OneDrive\\Desktop\\doto.txt" #dosyanın taşınacağı yeri belirler

try:
    if os.path.exists(hedef):
        print("Burada zaten bir dosya var")
    else:
        os.replace(kaynak , hedef)
        print(kaynak +" başarıyla taşındı")
except StopAsyncIteration:
    print("Böyle bir dosya bulunmadı :(")