# 2D listeler = listelerin içinde listeler barındırmasıdır

içecekler = ["kola", "fanta", "sprite"]
yemekler = ["pizza", "hamburger", "makarna"]
tatlılar = ["dondurma", "baklava", "künefe"]

menu = [içecekler, yemekler, tatlılar]  # 2D liste oluşturma

print(menu)  # 2D listeyi yazdırır. Tüm elemanları gösterir
print(menu[0])  # 2D listenin ilk alt listesini yazdırır. İçindeki elemanları gösterir
print(menu[0][1])  # 2D listenin ilk alt listesinin ikinci elemanını yazdırır. Tek bir elemanı gösterir