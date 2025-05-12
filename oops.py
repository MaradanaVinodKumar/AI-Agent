from abc import ABC, abstractmethod

# 1. CLASS & OBJECT
# A class is a blueprint. An object is an instance of the class.
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f"The {self.color} {self.brand} is driving.")

# 2. ENCAPSULATION
# Encapsulation hides internal data using private variables and provides access through methods.
class BankAccount:
    def __init__(self):
        self.__balance = 0  # private variable (double underscore)

    def deposit(self, amount):
        self.__balance += amount  # internal logic is hidden

    def get_balance(self):
        return self.__balance  # access controlled via method

# 3. INHERITANCE
# A child class inherits behavior from the parent class and can override it.
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")  # overriding parent method

# 4. POLYMORPHISM
# Polymorphism allows the same method name to behave differently based on the object.
class Cat:
    def sound(self):
        print("Meow")

class AnotherDog:
    def sound(self):
        print("Bark")

def make_sound(animal):
    animal.sound()  # Works for any object with a sound() method

# Example usage of polymorphism
cat = Cat()
dog = AnotherDog()

ex=make_sound(cat).sound()  # Output: Meow 
ex2=make_sound(dog).sound()  # Output: Bark


# 5. ABSTRACTION
# Abstraction hides complex implementation and shows only essential features.
class Shape(ABC):  # Abstract Base Class
    @abstractmethod
    def area(self):
        pass  # no implementation here

class Circle(Shape):
    def area(self):
        radius = 5
        return 3.14 * radius * radius  # implementation provided by subclass

# MAIN PROGRAM
if __name__ == "__main__":
    print("=== CLASS & OBJECT ===")
    my_car = Car("Toyota", "Red")
    my_car.drive()  # Output: The Red Toyota is driving.

    print("\n=== ENCAPSULATION ===")
    account = BankAccount()
    account.deposit(100)
    print("Balance:", account.get_balance())  # Output: Balance: 100

    print("\n=== INHERITANCE ===")
    a = Animal()
    d = Dog()
    a.speak()  # Output: Animal makes a sound
    d.speak()  # Output: Dog barks

    print("\n=== POLYMORPHISM ===")
    make_sound(Cat())       # Output: Meow
    make_sound(AnotherDog())  # Output: Bark

    print("\n=== ABSTRACTION ===")
    c = Circle()
    print("Area of circle:", c.area())  # Output: 78.5
