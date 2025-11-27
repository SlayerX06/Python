# Tuple = birden fazla değeri tek bir değişkende saklamak için kullanılır
# Tuple'lar parantez () içinde tanımlanır ve elemanlar virgül ile ayrılır
# Tuple'ların elemanlarına indeks numaraları ile erişilir, indeks numaraları 0'dan başlar
# Tuple'lar değiştirilemez (immutable) yani elemanları değiştirilemez

student = ("İbrahim", 25, "Mühendis",)
print(student.count("İbrahim")) # tuple içinde belirli bir elemanın kaç kez geçtiğini sayar
print(student.index("Mühendis")) # tuple içinde belirli bir elemanın indeks numarasını verir

for i in student: # tuple içindeki her eleman için döngü
    print(i) # elemanı yazdırır

if "Mühendis" in student: # tuple içinde belirli bir eleman var mı kontrol eder
    print("Evet, Mühendis var") # eleman varsa yazdırır     