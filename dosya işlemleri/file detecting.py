import os # dosya işlemleri için os modülünü içe aktar

patch = "C:\\Users\\CASPER\\OneDrive\\Desktop\\İlk Dosya\\dosya" # kontrol edilecek dosya veya klasörün yolu

if os.path.exists(patch): # dosya veya klasörün var olup olmadığını kontrol et
    print("Dosya veya klasör mevcut.")
    if os.path.isfile(patch): # dosya mı klasör mü kontrol et
        print("Bu bir dosyadır.")
    elif os.path.isdir(patch):
        print("Bu bir klasördür.")
else:
    print("Dosya veya klasör mevcut değil.")