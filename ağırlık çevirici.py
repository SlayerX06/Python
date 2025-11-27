ağırlık = float(input("Ağırlık giriniz: "))
birim = input("Birim giriniz (K veya L): ")

if birim == "K":
    ağırlık = ağırlık * 2.205
    birim = ("Lbs. ")
    print("Sizin kilonuz "+ str(round(ağırlık, 2)) +str(birim) )
          
elif birim == "L":
    ağırlık = ağırlık / 2.205
    birim = ("Kg. ")
    print("Sizin kilonuz "+ str(round(ağırlık, 2)) +str(birim))
          
else:
    print("Birim geçersiz")

   