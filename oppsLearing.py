class Car:
    def __init__(self):
        self.__Name = "No found!"
        self.Brand = "RR"

    def SetName(self, name):
        self.__Name = name

    def CarName(self):
        print(f"Car Name: {self.__Name}")



    
print("=== CLASS & OBJECT ===")

def Main():
    my_car = Car()
    my_car.SetName("Toyota")
    my_car.CarName()  # Output: Car Name: Toyota

    print(f"Card Brand: {my_car.Brand}")
    print(f"Card Brand: {my_car.__Name}")

Main()