

```markdown
# Object-Oriented Programming (OOP) in Python

A brief introduction to object-oriented programming concepts in Python.

## Table of Contents
- [Introduction](#introduction)
- [Classes](#classes)
- [Objects](#objects)
- [Inheritance](#inheritance)
- [Encapsulation](#encapsulation)
- [Polymorphism](#polymorphism)
- [Example](#example)

## Introduction

Object-oriented programming (OOP) is a programming paradigm that uses objects to structure code. In Python, everything is an object, and understanding OOP is fundamental for effective Python programming.

## Classes

A class is a blueprint for creating objects. It defines a set of attributes and methods that the objects created from the class will have.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"
```

## Objects

An object is an instance of a class. It is a concrete entity based on the class, with specific values assigned to its attributes.

```python
# Creating an instance of the Dog class
my_dog = Dog(name="Buddy", age=3)

# Accessing attributes
print(my_dog.name)  # Output: Buddy

# Calling methods
print(my_dog.bark())  # Output: Woof!
```

## Inheritance

Inheritance allows a class to inherit attributes and methods from another class. It promotes code reusability.

```python
class Labrador(Dog):
    def swim(self):
        return "Swimming!"

# Creating an instance of the Labrador class
my_labrador = Labrador(name="Max", age=2)

# Inherited attributes and methods
print(my_labrador.name)  # Output: Max
print(my_labrador.bark())  # Output: Woof!
print(my_labrador.swim())  # Output: Swimming!
```

## Encapsulation

Encapsulation refers to restricting access to certain attributes or methods. It helps in hiding the implementation details.

```python
class Circle:
    def __init__(self, radius):
        self.__radius = radius  # Encapsulated attribute

    def area(self):
        return 3.14 * self.__radius ** 2
```

## Polymorphism

Polymorphism allows objects of different classes to be treated as objects of a common base class. It promotes flexibility in code.

```python
# Polymorphic function
def animal_sound(animal):
    return animal.bark()

# Using polymorphism with Dog and Labrador instances
print(animal_sound(my_dog))        # Output: Woof!
print(animal_sound(my_labrador))   # Output: Woof!
```

