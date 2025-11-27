# Set = birden fazla değeri tek bir değişkende saklamak için kullanılır
# Set'ler süslü parantez {} içinde tanımlanır ve elemanlar virgül ile ayrılır
# Set'lerin elemanlarına erişim, indeks numarası ile değil, elemanın kendisi ile yapılır
# Set'ler değiştirilebilir (mutable) yani elemanları değiştirilebilir
# Set'ler sırasızdır (unordered) yani elemanların belirli bir sırası yoktur ve indeks numarası yoktur
# Set'ler aynı elemandan birden fazla bulundurmaz, yani her eleman benzersizdir


aletler = {"kalem", "silgi", "defter", "kitap", "çanta"}
dersler = {"matematik", "fizik", "kimya", "biyoloji", "tarih"}

#aletler.add("bilgisayar") # sete yeni bir eleman ekler
#aletler.remove("defter") # setten bir eleman çıkarır
#aletler.clear() # setin tüm elemanlarını çıkarır
#aletler.update(dersler) # bir setin elemanlarını başka bir sete ekler

çalışma_masası = aletler.union(dersler) # iki setin elemanlarını birleştirir ve yeni bir set oluşturur  

for alet in çalışma_masası: # setteki her eleman için döngü
    print(alet) # elemanı yazdırır
print(aletler.difference(dersler)) # bir sette olup diğer sette olmayan elemanları yazdırır
print(aletler.intersection(dersler)) # iki sette ortak olan elemanları yaz
