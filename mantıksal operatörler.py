ehliyet = False
araba =    True

if ehliyet and araba:      #and ile iki şartın da olması gerekir
    print("Araba kullanabilirsin")

elif araba and not ehliyet:   # not değişkenin değilini alır
    print("Kursumuza kaydolabilirsin")

elif araba or ehliyet:   #or ile bir tne true yeterlidir
    print("Arabaya az kaldı")

else:
    print("Arabaya daha çok var")