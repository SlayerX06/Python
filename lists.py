# Lists = listeler bir değişkene birden fazla değer atamak için kullanılır
# listeler köşeli parantez [] içinde tanımlanır ve elemanlar virgül ile ayrılır
# listelerin elemanlarına indeks numaraları ile erişilir, indeks numaraları 0'dan başlar
# listeler değiştirilebilir (mutable) yani elemanları eklenebilir, çıkarılabilir veya değiştirilebilir

yemekler = ["kebap", "pizza", "hamburger", "makarna", "salata"]

#print(yemekler) # listeyi yazdırır
#print(yemekler[0]) # listenin ilk elemanını yazdırır
#listede olandan fazla bir eleman çağırmak istersek hata verir
#listelerle işlem yapmak için . (nokta) operatörü kullanılır


yemekler.append("lahmacun") # listeye yeni bir eleman ekler
yemekler.remove("salata") # listeden bir eleman çıkarır
yemekler.pop() # listeden son elemanı çıkarır
yemekler.insert(1, "döner") # listeye belirli bir indekse eleman ekler
yemekler.sort() # listeyi alfabetik olarak sıralar


for yemek in yemekler: # listedeki her eleman için döngü
    print(yemek) # elemanı yazdırır

