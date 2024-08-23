class Animal():
    def make_sound(self):
        print("Some generic sound")
class Dog(Animal):
    def make_sound(self):
        print("Woof")
class Cat(Animal):
    def make_sound(self):
        print("Meow")
def animal_sound(*animal):
    for a in animal:
        a.make_sound()
C1=Cat()
C2=Cat()
C3=Cat()
C4=Cat()
C5=Cat()
C6=Cat()
D1=Dog()
D2=Dog()
D3=Dog()
D4=Dog()
D5=Dog()
D6=Dog()
D7=Dog()
D8=Dog()
animal_sound(C1,C2,C3,C4,C5,C6,D1,D2,D3,D4,D5,D6,D7,D8)