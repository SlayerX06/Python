from car import Car

car_1 = Car("Toyota", "Corolla", 2020, "Kırmızı")
car_2 = Car("Ford", "Mustang", 2022, "Mavi") 

#car_1.tekerler=2 #classlar default değerin yanında elle kendilerine değer atayabiliriz

Car.tekerler = 2 #tüm class dosyasındaki bir genel değeri değiştirirsek bundan sonraki değerler yeni deafult değeri alır

print(car_1.tekerler)
print(car_2.tekerler)