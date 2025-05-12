// 1. CLASS & OBJECT
// A class is a blueprint; objects are created from that blueprint.
class Car {
    String brand;
    String color;

    Car(String brand, String color) {
        this.brand = brand;
        this.color = color;
    }

    void drive() {
        System.out.println("The " + color + " " + brand + " is driving.");
    }
}

// 2. ENCAPSULATION
// Encapsulation protects data using private fields and public getters/setters.
class BankAccount {
    private int balance = 0;

    void deposit(int amount) {
        balance += amount;
    }

    int getBalance() {
        return balance;
    }
}

// 3. INHERITANCE
// Inheritance allows one class to acquire properties and methods of another.
class Animal {
    void speak() {
        System.out.println("Animal makes a sound");
    }
}

class Dog extends Animal {
    @Override
    void speak() {
        System.out.println("Dog barks");  // Method overriding
    }
}

// 4. POLYMORPHISM
// Polymorphism allows objects to take many forms; interfaces help achieve this.
interface Soundable {
    void sound();
}

class Cat implements Soundable {
    public void sound() {
        System.out.println("Meow");
    }
}

class AnotherDog implements Soundable {
    public void sound() {
        System.out.println("Bark");
    }
}

class SoundTest {
    static void makeSound(Soundable animal) {
        animal.sound();  // Calls sound() on any Soundable object
    }
}

// 5. ABSTRACTION
// Abstract classes define method signatures without implementations.
abstract class Shape {
    abstract double area();  // Abstract method
}

class Circle extends Shape {
    double area() {
        double radius = 5;
        return 3.14 * radius * radius;  // Concrete implementation
    }
}

// MAIN CLASS TO RUN EVERYTHING
public class OOPConcepts {
    public static void main(String[] args) {
        System.out.println("=== CLASS & OBJECT ===");
        Car car = new Car("Toyota", "Red");
        car.drive();

        System.out.println("\n=== ENCAPSULATION ===");
        BankAccount account = new BankAccount();
        account.deposit(100);
        System.out.println("Balance: " + account.getBalance());

        System.out.println("\n=== INHERITANCE ===");
        Animal a = new Animal();
        Dog d = new Dog();
        a.speak();  // Animal makes a sound
        d.speak();  // Dog barks

        System.out.println("\n=== POLYMORPHISM ===");
        SoundTest.makeSound(new Cat());         // Meow
        SoundTest.makeSound(new AnotherDog());  // Bark

        System.out.println("\n=== ABSTRACTION ===");
        Shape c = new Circle();
        System.out.println("Area of circle: " + c.area());  // 78.5
    }
}
