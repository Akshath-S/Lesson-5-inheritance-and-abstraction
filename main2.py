from abc import ABC,abstractmethod
class animal(ABC):
    def move(self):
        pass

class human(animal):
    def move(self):
        print("move around")

h=human()
h.move()

class snake(animal):
    def move(self):
        print("crawl")

s=snake()
s.move()

class Lion(animal):
    def move(self):
        print("move around")

L=Lion()
L.move()
