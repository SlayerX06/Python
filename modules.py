#modüller = python dosyalarında kullanılan ve belirli işlevleri yerine getiren önceden yazılmış kod parçacıklarıdır.
#modüller, kodunuzu daha düzenli ve yönetilebilir hale getirmek için kullanılır.
#modüller bir dosya içinde tanımlanabilir veya harici olarak yüklenebilir.
#mödüllersayesinde başka bir dosyada tanımlanmış fonksiyonları, sınıfları ve değişkenleri kullanabiliriz.

#import modules_alt as malt #modules_alt.py dosyasını import eder ve içindeki fonksiyonları kullanmamızı sağlar
# as malt ifadesi ile modules_alt modülünü malt olarak kısaltıyoruz

from modules_alt import merhaba, bye #modules_alt.py dosyasından sadece merhaba ve bye fonksiyonlarını import eder
#bu şekilde sadece ihtiyacımız olan fonksiyonları import edebiliriz ve modül adı ile çağırmak zorunda kalmayız
# import kısmından sonra * kullanarak tüm fonksiyonları import edebiliriz

merhaba() #modules_alt dosyasındaki merhaba fonksiyonunu çağırır

#malt.merhaba() #modules_alt dosyasındaki merhaba fonksiyonunu çağırır
#malt.bye() #modules_alt dosyasındaki bye fonksiyonunu çağırır

#internette python modul index diye aratarak hazır olarak yazılmış modülleri bulabiliriz