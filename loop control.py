# loop control statements = break, continue, pass
# break = döngüyü sonlandırır
# continue = döngüyü sonlandırmadan bir sonraki adıma geçer
# pass = hiçbir işlem yapmadan bir sonraki adıma geçer

while True:
    isim = input("İsim giriniz: ")
    if isim != "":
        break
# bu kod kullanıcıdan isim girmesini ister ve boş bırakırsa tekrar sorar, isim girilince döngüden çıkar

telefon = "123-456-7890"
for i in telefon:
   if i == "-":
       continue #eğer i değişkeni "-" ise bu adıma geçmeden döngünün başına döner print(i, end="") #end="" komutu printin sonuna boşluk ekler ve alt satıra geçmesini engeller
   print(i, end="") #end="" komutu printin sonuna boşluk ekler ve alt satıra geçmesini engeller
# bu kod telefon numarasını tek tek yazdırır ve "-" işaretlerini atlar

for i in range(1, 21):
    if i == 13:
        pass #i değişkeni 13 olduğunda hiçbir işlem yapmadan döngünün başına döner
    else:
        print(i)