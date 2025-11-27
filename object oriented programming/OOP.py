# oop = Object Oriented Programming, nesne yönelimli programlama
# OOP, programlamada nesneleri ve bu nesnelerin etkileşimlerini kullanarak yazılım geliştirme yaklaşımıdır. 
# OOP cisimsel dünyayı modellemek için kullanılır ve kodun daha düzenli, yeniden kullanılabilir ve bakımı kolay olmasını sağlar.

from car import Car  # car.py dosyasından Car sınıfını import eder

car_1 = Car("Toyota", "Corolla", 2020, "Kırmızı")  # Car sınıfından bir nesne oluşturur
car_2 = Car("Ford", "Mustang", 2022, "red")

print(car_2.make)  # Nesnenin make özelliğini yazdırır
print(car_2.model)  # Nesnenin model özelliğini yazdırır
print(car_2.year)  # Nesnenin year özelliğini yazdırır
print(car_2.color)  # Nesnenin color özelliğini yazdırır 

car_2.drive()
car_2.stop()