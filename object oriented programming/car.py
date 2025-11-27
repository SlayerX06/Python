class Car:

    tekerler = 4 #bu atama ile oluşacak tüm modellere otomatik olarak 4 teker atamış oluruz

    def __init__(self, make, model, year, color): # Yapıcı metod, nesne oluşturulduğunda çağrılır
        self.make = make  #instance variables her class kendine özgü bir değer alır
        self.model = model  #instance variables
        self.year = year  #instance variables
        self.color = color  #instance variables

    def drive(self): # self parametresi, yöntemin çağrıldığı nesneyi temsil eder
        print("The "+self.model +" is driving.")

    def stop(self):
        print("The car has stopped.")
