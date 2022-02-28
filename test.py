#!/usr/bin/env python3
from abc import ABC, abstractmethod

class Animal(ABC): # inherit from ABC (Abstract base class)
    @abstractmethod # Decorator to define an abstract method
    def feed(self):
        pass

class Panda(Animal):
    def feed(self):
        print("Feeding a panda with some tasty bamboo!")
    def do(self, action, time):
        print(f"{action}, a panda! at {time}")
class Snake(Animal):
    def feed(self):
        print("Feeding a Snake with some tasty bamboo!")
    def do(self, action, time):
        print(f"{action}, a snake! at {time}")

zoo = [Panda(), Snake()]
for animal in zoo:
    animal.feed()
    animal.do(action="feeding", time="10.10 PM")