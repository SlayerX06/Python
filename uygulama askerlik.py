okul = input("Okuyor musnuz? (evet: e, hayır: h)")
yas = int(input("Yaşınızı giriniz"))

if okul=="h" and yas > 18:
    print("Askere gitme yaşınız gelmiştir")

elif okul=="e" and yas > 18:
    print("Okulunuz bittiğinde askere geleceksiniz")

else:
    print("Askerlik yaşınız daha gelmedi")