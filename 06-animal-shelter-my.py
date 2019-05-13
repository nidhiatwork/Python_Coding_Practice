""" 
Implement a cat and dog queue for an animal shelter.
"""

class AnimalShelter:
      def __init__(self):
            self.cats = []
            self.dogs = []

      def enqueue(self,animal):
            if animal.__class__==Cat:
                  self.cats.append(animal)
            else:
                  self.dogs.append(animal)

      def dequeueCat(self):
            if len(self.cats)>0:
                  self.cats = self.cats[1:]

      def dequeueDog(self):
            if len(self.dogs)>0:
                 self.dogs = self.dogs[1:]

      def dequeueAny(self):
            if len(self.cats): self.dequeueCat()
            else: self.dequeueDog()

class Animal:
      def __init__(self,name):
        self.name = name

class Cat(Animal): pass
class Dog(Animal): pass

c = Cat("Cat1")
d = Dog("Dog1")
a = AnimalShelter()
a.enqueue(c)
a.enqueue(d)
a.dequeueAny()
a.enqueue(c)
