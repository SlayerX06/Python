# copyfile() = bir dosyanın içeriğini kopyalar
# copy() = copyfile() + permission mode + destination can be a directory
#copy2() = copy() + copies metadata (files creation and modification time)

import shutil

shutil.copyfile("test.txt", "copy.txt") #buraya yazdığımız ilk dosya kaynak ikinici dosya hedeftir. 
# diğer copy komutları da bu düzenle çalışır duruma uygun olan kod seçilir

