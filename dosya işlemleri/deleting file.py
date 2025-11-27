import os
import shutil


try:
    os.remove("C:\\Users\\CASPER\\OneDrive\\Desktop\\İlk Dosya\\test.txt") #dosya yolunu verdiğmiz dosyayı siler
    print("Dosya silindi")
    #os.rmdir() #boş dosyalar için kullanılan komuttur. yetki olmadığında kullanılır. dosya boş değilse kullanılamaz
    #shutil.rmtree dolu olan dosyaları silebilen komuttur
except FileNotFoundError:
    print("Böyle bir dosya yok!")