#!/usr/bin/env python3

def greet_programmer():
    print (f"Hello, programmer!")

def greet(name = "Naureen"):
    print (f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    print(num1 + num2)
    return (num1 + num2)

    sum = add(1,2)

def halve(number):
    if not isinstance(number, (int, float)):
      return None
    return number/2
print(halve(100))
