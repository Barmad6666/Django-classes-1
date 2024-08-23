class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
    def change_age(self, new_age):
        self.age = new_age
    def __str__(self):
        return f"name: {self.name}, age: {self.age}"
name, age = input().split()
age = int(age)
new_age = int(input())
person = Person(name, age)
person.change_age(new_age)
print(person)
